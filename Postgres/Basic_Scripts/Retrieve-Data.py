#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras
import sys


def fetch_option1():
    # Set the connection
    connection = None

    try:
        # Connect to db
        connection = psycopg2.connect("dbname='testdb' user='manuel'")

        # Fetch the curser and execute the query
        curser = connection.cursor()
        curser.execute("SELECT * FROM Cars")

        # Get the results
        rows = curser.fetchall()

        # Iterate through the result
        for row in rows:
            print (row)

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def fetch_option2():
    connection = None
    try:
        connection = psycopg2.connect("dbname='testdb' user='manuel'")
        curser = connection.cursor()
        curser.execute("SELECT * FROM Cars")

        # fetch and print the result row by row
        while True:
            row = curser.fetchone()
            if row == None:
                break
            print (row[0], row[1], row[2])

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)

    finally:
        if connection:
            connection.close()


def fetch_option3():
    connection = None
    try:
        connection = psycopg2.connect("dbname='testdb' user='manuel'")
        curser = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curser.execute("SELECT * FROM Cars")

        # fetch and print the result row by row
        rows = curser.fetchall()
        for row in rows:
            print (row)
            #print ("%s %s %s" % (row["id"], row["name"], row["price"]))

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)

    finally:
        if connection:
            connection.close()




if __name__ == '__main__':
    fetch_option1()
    fetch_option2()
    fetch_option3()