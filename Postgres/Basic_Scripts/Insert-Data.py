#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


connection = None

try:

    connection = psycopg2.connect("dbname='testdb' user='manuel'")

    curser = connection.cursor()

    # Creates a Cars table with Id as PKey, Name as string of length 20 and price as integer
    curser.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    # Insert some data to cars
    curser.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    curser.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    curser.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    curser.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    curser.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    curser.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    curser.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    curser.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

    # Commit the changes to the database
    connection.commit()

# If there is an Error
except psycopg2.DatabaseError as e:

    # If connection was established, rollback and cancel the commands
    if connection:
        connection.rollback()

    # Print the Erro
    print ('Error %s' % e)
    sys.exit(1)

# Close the db connection
finally:
    if connection:
        connection.close()