#!/usr/bin/python3
"""Here goes the code"""
import MySQLdb
import sys


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id=cities.state_id")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
