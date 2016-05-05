#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def createTables():
    connection = None
    try:
        connection = psycopg2.connect("dbname='countrytest' user='manuel'")
        curser = connection.cursor()
        # Create four tables in the database:
        curser.execute("CREATE TABLE countries ("
                       "country_code char(2) PRIMARY KEY,"
                       "country_name text UNIQUE"
                       ")")
        curser.execute("CREATE TABLE cities ("
                       "city_name text NOT NULL,"
                       "country_code char(2) REFERENCES countries,"
                       "PRIMARY KEY (country_code, city_name)"
                       ")")
        curser.execute("CREATE TABLE places ("
                       "place_id SERIAL PRIMARY KEY,"
                       "name varchar(255),"
                       "type char(10) CHECK (type in ('restaurant', 'bar', 'club', 'other')) DEFAULT 'other',"
                       "city_name text NOT NULL,"
                       "country_code char(2),"
                       "FOREIGN KEY (country_code, city_name) REFERENCES cities (country_code, city_name) MATCH FULL"
                       ")")
        curser.execute("CREATE TABLE events ("
                       "event_id SERIAL PRIMARY KEY,"
                       "title varchar(255),"
                       "starts timestamp,"
                       "ends timestamp,"
                       "place_id integer NOT NULL,"
                       "FOREIGN KEY (place_id) REFERENCES places (place_id) MATCH FULL"
                       ")")
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


def populateTables():
    # Artifical Data:
    countries = (
    ('de', 'Germany'),
    ('uk', 'United Kingdom'),
    ('us', 'United States'),
    ('au', 'Australia'),
    ('fr', 'France'),
    ('es', 'Spain'),
    ('fi', 'Finland'),
    ('dk', 'Denmark')
    )

    cities = (
    ('Berlin', 'de'),
    ('Hamburg', 'de'),
    ('New York', 'us'),
    ('London', 'uk'),
    ('Dallas', 'us'),
    ('San Fransisco', 'us'),
    ('Munich', 'de'),
    ('Sydney', 'au'),
    ('Helsinki', 'fi'),
    ('Copenhagen', 'dk'),
    ('Paris', 'fr'),
    ('Madrid', 'es'),
    ('Chicago', 'us')
    )

    places = (
    ('Club A','club','de','Berlin'),
    ('Restaurant B','restaurant','de','Munich'),
    ('Bar C','bar','uk','London'),
    ('Club B','club','fr','Paris'),
    ('Restaurant A','restaurant','de','Berlin'),
    ('Bar A','bar','us','New York'),
    ('Club C','club','us','New York'),
    ('Bar D','bar','uk','London'),
    ('Club E','club','de','Berlin'),
    ('Restaurant C','restaurant','au','Sydney'),
    ('Bar A','bar','us','Dallas')
    )

    events = (
    ('Band 1','2015-01-15 20:00:00','2015-01-15 20:30:00','1'),
    ('Band 2','2015-01-19 20:15:00','2015-01-19 22:00:00','10'),
    ('Band 3','2015-02-23 20:30:00','2015-02-23 22:50:00','11'),
    ('Theater 1','2015-04-05 19:00:00','2015-04-05 20:15:00','3'),
    ('Theater 2','2015-05-14 19:20:00','2015-05-14 20:20:00','5'),
    ('Theater 3','2015-06-24 18:30:00','2015-06-24 20:00:00','1'),
    ('Band 1','2015-02-25 21:00:00','2015-02-25 22:15:00','7'),
    ('Band 2','2015-04-15 21:30:00','2015-04-15 22:00:00','8'),
    ('Band 3','2015-08-13 22:05:00','2015-08-13 23:30:00','11'),
    ('Soiree 1','2016-01-01 18:00:00','2016-01-01 20:00:00','1'),
    ('Soiree 2','2016-01-23 19:05:00','2016-01-23 21:30:00','4'),
    ('Soiree 3','2016-03-28 20:00:00','2016-03-28 20:15:00','5')
    )

    connection = None
    try:
        #Establish the connection
        connection = psycopg2.connect("dbname='countrytest' user='manuel'")
        curser = connection.cursor()

        # Insert Data into the different Data tables:
        query_countries = "INSERT INTO countries (country_code, country_name) VALUES (%s,%s)"
        query_cities = "INSERT INTO cities (city_name, country_code) VALUES (%s,%s)"
        query_places = "INSERT INTO places (name, type, country_code, city_name) VALUES (%s,%s,%s,%s)"
        query_events = "INSERT INTO events (title, starts, ends, place_id) VALUES (%s,%s,%s,%s)"
        curser.executemany(query_countries, countries)
        curser.executemany(query_cities, cities)
        curser.executemany(query_places, places)
        curser.executemany(query_events, events)

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





if __name__ == '__main__':
    createTables()
    populateTables()