#!/usr/bin/python3


import sys, MySQLdb
"""
Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    conn = db.cursor()

    user_input = sys.argv[4]

    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    user_input = sys.argv[4]

    conn.execute(query, (user_input,))

    result = conn.fetchall()

    [print(states) for states in result]

    conn.close()
    db.close()
