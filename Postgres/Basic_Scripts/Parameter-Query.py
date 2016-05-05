#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def parameter_query(price, id):
    connection = None
    try:
        connection = psycopg2.connect("dbname='testdb' user='manuel'")
        curser = connection.cursor()
        curser.execute("UPDATE Cars SET Price=%s WHERE Id=%s", (price, id))
        connection.commit()
        print ("Number of rows updated: %d" % curser.rowcount)

    except psycopg2.DatabaseError as e:
        if connection:
            connection.rollback()
        print ('Error %s' % e)
        sys.exit(1)

    finally:
        if connection:
            connection.close()

def select_entry(id):
    connection = None
    try:
        connection = psycopg2.connect("dbname='testdb' user='manuel'")
        curser = connection.cursor()
        curser.execute("SELECT * FROM Cars WHERE Id=%s",(id))
        connection.commit()
        print ("Number of rows updated: %d" % curser.rowcount)

    except psycopg2.DatabaseError as e:
        if connection:
            connection.rollback()
        print ('Error %s' % e)
        sys.exit(1)

    finally:
        if connection:
            connection.close()





if __name__ == '__main__':
    parameter_query(62300,1)