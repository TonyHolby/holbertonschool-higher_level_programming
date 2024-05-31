#!/usr/bin/python3
import requests
import csv
""" Defines a method named fetch_and_print_posts that displays a list of
    dictionary if the status code of the request is succesful.
"""


def fetch_and_print_posts():
    """ Displays a list of dictionary if status code is equal to 200. """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        fetched_data = response.json()
        for data in fetched_data:
            print(data.get("title"))


""" Defines a method named fetch_and_save_posts that converts structured data
    into CSV format.
"""


def fetch_and_save_posts():
    """ Saves data in a CSV file if status code is equal to 200. """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code == 200:
        fetched_data = response.json()
        posts = []
        for data in fetched_data:
            posts.append({"id": data.get("id"), "title": data.get("title"), "body": data.get("body")})
        with open("posts.csv", 'w', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
