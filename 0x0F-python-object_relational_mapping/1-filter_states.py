#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
