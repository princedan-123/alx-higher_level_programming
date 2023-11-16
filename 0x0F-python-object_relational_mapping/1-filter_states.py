#!/usr/bin/python3
"""Prints only states that begin with upercase N from a database."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    connection = MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            )
    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
            )
    result = cursor.fetchall()
    for row in result:
        print(row)
