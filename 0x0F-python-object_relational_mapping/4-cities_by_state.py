#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
argv:
1 = username
2 = password
3 = database
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
