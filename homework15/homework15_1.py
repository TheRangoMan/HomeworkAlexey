from pprint import pprint
import mysql.connector
from mysql.connector import cursor


class Database:
    def __init__(self, host, user, password, database):
        self.connect = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connect.cursor()
    
    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.connect.commit()
    
    def close(self):
        self.cursor.close()
        self.connect.close()


sqlconnection = Database(host='localhost', user='user2064', password='!QA2ws3ed',database = "db2064")


