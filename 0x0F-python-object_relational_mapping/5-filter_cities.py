#!/usr/bin/python3
"""Here goes the code"""
import MySQLdb
import sys


if __name__ == "__main__":
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

    cursor.execute("SELECT cities.name FROM\
                cities INNER JOIN states ON states.id=cities.state_id\
                WHERE states.name=%s", (state_name,))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    formatted_cities = ", ".join(city_names)

    print(formatted_cities)

    cursor.close()
    db.close()
