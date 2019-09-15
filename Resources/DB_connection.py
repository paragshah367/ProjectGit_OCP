# coding=utf-8

import mysql.connector
from mysql.connector import Error


def db_conn(query):
    """This function connects to QA db"""
    try:
        mydb = mysql.connector.connect(
          host='localhost',
          port='3308',
          user='dev',
          passwd='dev')

        mycursor = mydb.cursor()
        # mycursor.execute('SELECT * FROM subscription.subscriptionplan order by id desc limit 2;')
        mycursor.execute(query)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    except Error as e:
        print('Error occured -', e)

    finally:
        if mydb.is_connected():
            mydb.close()
            print('DB Connection closed')


query = 'SELECT * FROM subscription.subscriptionplan order by id desc limit 2;'
db_conn(query)
