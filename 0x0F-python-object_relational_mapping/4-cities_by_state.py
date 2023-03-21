#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    # create a cursor
    cursor = db.cursor()
    # execute the SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    # fetch all the rows
    rows = cursor.fetchall()
    # print the rows
    if rows is not None:
        for row in rows:
            print(row)
    # close the cursor and database connection
    cursor.close()
    db.close()
