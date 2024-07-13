#!/usr/bin/python3

""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name,
                           charset="utf8")

    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    conn.close()
