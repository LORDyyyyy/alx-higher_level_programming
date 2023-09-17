#!/usr/bin/python3
"""Here goes the code"""
import MySQLdb
import sys


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = "SELECT * FROM states\
            WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(state_name)

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
