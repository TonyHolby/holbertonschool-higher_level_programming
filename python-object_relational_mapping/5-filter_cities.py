#!/usr/bin/python3

""" A script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    try:
        db_connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        cursor = db_connect.cursor()
        query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """
        cursor.execute(query, (state_name,))
        query_rows = cursor.fetchall()
        cities = []
        for row in query_rows:
            cities.append(row[1])
        print(", ".join(cities))
    finally:
        cursor.close()
        db_connect.close()
