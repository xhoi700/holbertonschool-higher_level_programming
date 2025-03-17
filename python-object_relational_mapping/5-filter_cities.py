#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    que = "SELECT cities.name FROM cities\
                    JOIN states ON states.id=cities.state_id\
                    WHERE states.name LIKE BINARY %s\
                    ORDER BY cities.id ASC"
    cur.execute(que, (sys.argv[4], ))
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
