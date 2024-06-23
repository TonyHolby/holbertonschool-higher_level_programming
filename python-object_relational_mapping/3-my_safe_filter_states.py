#!/usr/bin/python3

""" A script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
    and that is safe from MySQL injections.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name_searched,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    finally:
        cursor.close()
        db.close()
