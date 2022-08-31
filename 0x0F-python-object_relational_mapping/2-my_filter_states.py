#!/usr/bin/python3
""" script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument
"""
from ctypes import string_at
import MySQLdb
import sys

""" This code not be executed when imported"""
if __name__ == "__main__":

    data_b = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = data_b.cursor()
    string_ex = "SELECT * FROM states WHERE name = '{}';".format(sys.argv[4])
    cur.execute(string_ex)
    rows = cur.fetchall()
    for row in rows:
        print(row)
