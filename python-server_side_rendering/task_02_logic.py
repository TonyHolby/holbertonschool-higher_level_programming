from flask import Flask, render_template, jsonify
import json
import os


app = Flask(__name__)

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
        with open(items_file, 'r') as f:
            data = json.load(f)
            list_of_items = data.get("items", [])
    except Exception as e:
        print(f"Error during read items.json: {e}")

    return render_template('items.html', items=list_of_items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
