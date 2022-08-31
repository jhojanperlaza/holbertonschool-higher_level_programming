#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

""" This code not be executed when imported"""
if __name__ == "__main__":

    data_b = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = data_b.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id=states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
