#!/usr/bin/python3
"""A script that lists all cities in a state from a database."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    with MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT states.id, cities.name, states.name FROM states\
                    JOIN cities ON states.id = cities.state_id"
                    )
        result = cursor.fetchall()
        for row in result:
            print(row)
