#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

# Building a set of triples with the Input for the db
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

# Set the connection
connection = None

try:
    # Connect to db
    connection = psycopg2.connect("dbname='testdb' user='manuel'")

    #Get the curser
    curser = connection.cursor()

    # Delete the 'old' table if exists
    curser.execute("DROP TABLE IF EXISTS Cars")

    # (Re)Create the table
    curser.execute("CREATE TABLE Cars(Id INT PRIMARY KEY, Name TEXT, Price INT)")

    # Build the overall query with the structure of the triples defined in cars
    query = "INSERT INTO Cars (Id, Name, Price) VALUES (%s, %s, %s)"

    # Execute the defined query with the set of the tuples
    curser.executemany(query, cars)
    connection.commit()

# Error catching
except psycopg2.DatabaseError as e:

    if connection:
        connection.rollback()

    print ('Error %s' % e)
    sys.exit(1)

# Close the db connection
finally:

    if connection:
        connection.close()