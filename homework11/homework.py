import random
from mysql.connector import cursor
import mysql.connector



mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()

winning = (10,21,13,14,28)

