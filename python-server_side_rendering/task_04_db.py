from flask import Flask, render_template, request, g
import json
import csv
import os
import sqlite3


app = Flask(__name__)
app.config['DATABASE'] = 'products.db'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def read_items():
    list_of_items = []
    items_file = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(items_file, 'r') as file:
            data = json.load(file)
            list_of_items = data.get("items", [])
    except Exception as e:
        print(f"Error during read items.json: {e}")

    return render_template('items.html', items=list_of_items)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    list_of_products = []
    error_message = None

    if source not in ['json', 'csv', 'sql']:
        error_message = "Wrong source"
    else:
        if source == 'json':
            source_file = os.path.join(os.path.dirname(__file__),
                                       'products.json')
            try:
                with open(source_file, 'r', encoding='utf-8') as json_file:
                    list_of_products = json.load(json_file)
            except Exception as e:
                error_message = f"Error reading products.json: {e}"

        elif source == 'csv':
            source_file = os.path.join(os.path.dirname(__file__),
                                       'products.csv')
            try:
                with open(source_file, newline='',
                          encoding='utf-8') as csv_file:
                    data_csv_file = csv.DictReader(csv_file)
                    for row in data_csv_file:
                        row['id'] = int(row['id'])
                        row['price'] = float(row['price'])
                        list_of_products.append(row)
            except Exception as e:
                error_message = f"Error reading products.csv: {e}"

        elif source == 'sql':
            try:
                conn = sqlite3.connect(app.config['DATABASE'])
                cursor = conn.cursor()
                query = "SELECT id, name, category, price FROM Products"
                cursor.execute(query)
                rows = cursor.fetchall()
                conn.close()
                
                list_of_products = [
                    {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
                    for row in rows
                ]
                
                if not list_of_products:
                    error_message = "Product not found"

            except Exception as e:
                error_message = f"Error accessing products.db: {e}"

    filtered_products = []
    if not error_message:
        if id:
            try:
                id = int(id)
                for product in list_of_products:
                    if product['id'] == id:
                        filtered_products.append(product)
                if not filtered_products:
                    error_message = "Product not found"
            except ValueError:
                error_message = "Invalid id format"
        else:
            filtered_products = list_of_products

    for product in filtered_products:
        for key in ["id", "name", "category", "price"]:
            if key not in product or product[key] is None:
                product[key] = "N/A"

    return render_template('product_display.html',
                           products_to_display=filtered_products,
                           error_message=error_message,
                           source=source)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
