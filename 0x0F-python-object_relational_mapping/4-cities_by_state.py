#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connectig to a MySQL database
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # Getting a Cursor in MySQL
    cur = db.cursor()
    # Executing MySQL Queries
    cur.execute("SELECT cities.id, cities.name, states.name
                FROM states
                INNER JOIN cities ON states.id=cities.state_id
                ORDER BY cities.id ASC")
    # Obtainig Query Results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close al cursors
    cur.close()
    # Close all batabases
    db.close()
