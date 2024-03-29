#!/usr/bin/python3
"""  lists all cities from the database
hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.name
        FROM states JOIN cities
        ON cities.state_id = states.id
        WHERE states.name=%s""", (sys.argv[4], ))
    query_rows = cur.fetchall()
    result = []
    for row in query_rows:
        result.append(row[0])
    print(*result, sep=', ')
    cur.close()
    conn.close()
