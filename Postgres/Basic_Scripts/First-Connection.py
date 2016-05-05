#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

#Initialize the connection to db variable
connection = None

try:
    # Try to connect to database and run database session
    connection = psycopg2.connect(database='testdb', user='manuel')
    # The connection returns an curser object, curser is used to traverse the records from the result set
    curser = connection.cursor()
    # The curser is used to execute the SQL statement
    curser.execute('SELECT version()')
    # Fetch the data. If the return is single line then use fetchone() method
    ver = curser.fetchone()
    print (ver)

# If Database error occurs, print the error and exit the program
except psycopg2.DatabaseError as e:
    print ('Error %s' % e)
    sys.exit(1)

# Close the database connection
finally:

    if connection:
        connection.close()


