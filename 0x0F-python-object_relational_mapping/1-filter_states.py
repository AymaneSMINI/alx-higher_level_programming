#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
import sys
user = sys.argv[1]
pw = sys.argv[2]
db = sys.argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=pw,
            db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states where name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
