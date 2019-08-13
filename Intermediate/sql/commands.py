'''
Created on Jun 25, 2019

@author: mrfox
'''
import mysql.connector
from mysql.connector import Error

def connect():
    """Connect to MySQL DB"""
    my_db_con = mysql.connector.connect(host='172.18.0.2',
                                        database='my_data',
                                        user='root',
                                        password='dbrpw')
    
    try:        
        if my_db_con.is_connected():
            print('Connection established')
        else:
            print("Couldn't establish connection.")
    
    except Error as e:
        print(e)
    
    finally:
        if my_db_con.is_connected():
            my_db_con.close()


connect()
        
