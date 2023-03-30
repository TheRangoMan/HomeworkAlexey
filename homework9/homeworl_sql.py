
from pprint import pprint
from mysql.connector import cursor
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost', user ='user2064', password = '!QA2ws3ed')
cursor = mydb.cursor()
query = 'SELECT * FROM db2064.income2;'
cursor.execute(query)
result = cursor.fetchall()
cursor.close()

pprint(result)