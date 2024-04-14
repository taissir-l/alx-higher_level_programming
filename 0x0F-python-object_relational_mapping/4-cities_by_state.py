#!/usr/bin/python3
'''selects all cities and their state in a database'''
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        cursor.execute(
            'SELECT cities.id, cities.name, states.name FROM cities' +
            ' INNER JOIN states ON cities.state_id = states.id' +
            ' ORDER BY cities.id ASC;'
        )

        a = cursor.fetchall()
        for i in a:
            print(i)
        db_connection.close()
