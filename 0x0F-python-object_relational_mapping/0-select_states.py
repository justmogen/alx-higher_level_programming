#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states")

    # Fetch the results and print them
    results = cursor.fetchall()
    for row in results:
        print(row)
