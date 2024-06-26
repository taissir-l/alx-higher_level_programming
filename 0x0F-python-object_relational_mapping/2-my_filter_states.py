#!/usr/bin/python3
''' selects rows with a name that matches the given argument'''
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        state_name = sys.argv[4]
        cursor.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
        )
        a = cursor.fetchall()
        for i in a:
            print(i)
        db_connection.close()
