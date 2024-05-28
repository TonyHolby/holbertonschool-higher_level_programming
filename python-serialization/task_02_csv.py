#!/usr/bin/env python3
import csv
import json

""" Defines a function named convert_csv_to_json that takes the CSV filename
    as its parameter and writes the JSON data to data.json.
"""


def convert_csv_to_json(csv_filename):
    """ Converts data into a dictionary list.
    
    Args:
        csv_filename: The name of the CSV file to convert.
    Returns:
        True if the conversion was successful, False on error.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = []
            for row in csv_reader:
                data_list.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)

        return True

    except FileNotFoundError:
        print("file not found")
        return False
    except Exception as e:
        print(f"Conversion error: {e}")
        return False
