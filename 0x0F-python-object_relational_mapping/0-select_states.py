#!/usr/bin/python3
# Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

import sys
import MySQLdb

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the database
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        sys.exit(1)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cursor.execute(query, ('%{}%'.format(state_name),))

    # Fetch the results and print them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

