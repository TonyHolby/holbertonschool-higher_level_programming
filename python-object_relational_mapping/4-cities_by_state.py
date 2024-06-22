#!/usr/bin/python3

""" A method that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
    and that is safe from MySQL injections.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
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
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
        cursor.execute(query)
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
    finally:
        cursor.close()
        db_connect.close()
