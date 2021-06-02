import mysql.connector
import json

def connect():
    host='sd-database.cpznaee3icow.us-east-1.rds.amazonaws.com'
    port='3306'
    user='admin'
    passwd='12345678'
    database='chinook'
    conn = mysql.connector.connect(host=host, port=port, user=user, passwd=passwd, database=database)
    
    return conn
