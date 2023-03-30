
from pprint import pprint
from mysql.connector import cursor
import mysql.connector
from homework_read import Textdata



mydb = mysql.connector.connect(
    host = 'localhost', user ='user2064', password = '!QA2ws3ed')
cursor = mydb.cursor()
query = 'SELECT income, month, year  FROM db2064.income2 ;'
cursor.execute(query)
result = cursor.fetchall()
cursor.close()

"""
with open('income.txt', 'w') as file:
    for row in result:
        file.write(str(row)+ '\n')

file.close()
mydb.close()
"""


t = Textdata().readfile('A:\\Python 2.0\\income.txt').createresult()

pprint(t.map)