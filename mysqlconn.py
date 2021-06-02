import mysql.connector
import json

conn = mysql.connector.connect(host='sd-database.cpznaee3icow.us-east-1.rds.amazonaws.com', port='3306', user='admin', passwd='12345678', database='chinook')

cursor = conn.cursor()
cursor.execute('select * from albums')

records = cursor.fetchall()

'''for i in records:
    print (f'{i[0]} - {i[1]}')'''

lista = [dict(zip(cursor.column_names, i)) for i in records]

print(json.dumps(lista, indent=4))
