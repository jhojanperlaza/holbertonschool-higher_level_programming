#!/usr/bin/python3
"""
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
link : https://stackoverflow.com/questions/7929364/python-
best-practice-and-securest-way-to-connect-to-mysql-and-execute-queries
"""
import MySQLdb
import sys

""" This code not be executed when imported"""
if __name__ == "__main__":

    data_b = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = data_b.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    """ is very important the , despues of sys.argv[4]"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
