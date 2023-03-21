#!/usr/bin/python3
"""
takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cursor.execute(query, (argv[4],))

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Now, let's print fetched result
    for row in results:
        print(row)
