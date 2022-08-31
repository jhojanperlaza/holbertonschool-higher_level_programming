#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


""" This code not be executed when imported"""
if __name__ == "__main__":

    data_b = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = data_b.cursor()
    cur.execute("SELECT cities.name FROM cities INNER\
        JOIN states ON states.name = %s AND\
        states.id=cities.state_id;", (sys.argv[4],))
    states = cur.fetchall()

    print(", ".join([state[0] for state in states]))
    # states is a array of tuples
