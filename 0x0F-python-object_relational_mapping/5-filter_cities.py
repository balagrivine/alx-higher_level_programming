#!/usr/bin/python3



"""
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    conn = db.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name = %s ORDER BY cities.id"

    conn.execute(query, (argv[4],))

    results = conn.fetchall()

    [print(row) for row in results]

    conn.close()
    db.close()
