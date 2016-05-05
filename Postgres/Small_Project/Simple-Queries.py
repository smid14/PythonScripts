#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def print_Result(rows,question):
    print ('-' * 500)
    print (question)
    print ('-' * 500)
    for row in rows:
        print (row)


def select_all():
    # Set the connection
    connection = None
    try:
        # Connect to db
        connection = psycopg2.connect("dbname='countrytest' user='manuel'")
        # Fetch the curser and execute the query
        curser = connection.cursor()
        curser.execute("SELECT * FROM countries")
        rows = curser.fetchall()
        print_Result(rows)

        curser.execute("SELECT * FROM cities")
        rows = curser.fetchall()
        print_Result(rows)

        curser.execute("SELECT * FROM places")
        rows = curser.fetchall()
        print_Result(rows)

        curser.execute("SELECT * FROM events")
        rows = curser.fetchall()
        print_Result(rows, 'All Data in Database')

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def executeQuery(query,question):
    connection = None
    try:
        # Connect to db
        connection = psycopg2.connect("dbname='countrytest' user='manuel'")
        curser = connection.cursor()
        curser.execute(query)
        rows = curser.fetchall()
        print_Result(rows,question)

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def createView():
    pass






if __name__ == "__main__":

    #select_all()

    executeQuery("SELECT cities.*, country_name "
                 "FROM cities INNER JOIN countries "
                 "ON cities.country_code = countries.country_code", 'Find the corresponding Country Name for all cities')

    executeQuery("SELECT places.place_id, places.name, places.type, cities.city_name "
                 "FROM places INNER JOIN cities "
                 "ON places.city_name = cities.city_name AND places.country_code = cities.country_code", 'Find the corresponding city for each place')

    executeQuery("SELECT events.*, places.place_id, places.name "
                 "FROM events INNER JOIN places "
                 "ON events.event_id = places.place_id", 'Find the place for each event')

    executeQuery("SELECT events.title, places.name, cities.city_name "
                 "FROM events, places, cities "
                 "WHERE events.place_id = places.place_id AND places.city_name = cities.city_name", 'Find the Place Name and city for each event')

    executeQuery("SELECT place_id,count(*) "
                 "FROM events GROUP BY place_id", 'Find the number of events for each place')

    executeQuery("SELECT place_id,count(*) "
                 "FROM events GROUP BY place_id HAVING count(*) > 1", 'Find the number of events greater than 1 for each place')

    executeQuery("SELECT place_id,count(*) "
                 "FROM events GROUP BY place_id HAVING count(*) > 1", 'Find the number of events greater than 1 for each place')
