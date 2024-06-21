#!/usr/bin/python3
import sys
import MySQLdb
""" A method that lists all states from the database hbtn_0e_0_usa. """


def list_states(mysql_username, mysql_password, database_name):
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(mysql_username, mysql_password, database_name)
