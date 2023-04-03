import random
from mysql.connector import cursor
import json
import mysql.connector
import random

mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "insert into db2064.myrecords (summa) values "
nonfirst = False



ticket_numbers = [i for i in range(1, 101)]


ticket_lines = [(i, j) for i in ticket_numbers for j in range(1, 6)]
random.shuffle(ticket_lines)


ticket_line_inserts = []
ticket_line_numbers_inserts = []

for i, ticket_line in enumerate(ticket_lines):
    ticket_line_inserts.append(f"INSERT INTO ticket_line (id, номер_билета) VALUES ({i + 1}, {ticket_line[0]})")
    ticket_line_numbers_inserts.append(f"INSERT INTO ticket_line_numbers (number, ticket_line_id) VALUES ({ticket_line[1]}, {i + 1})")

ticket_line_sql = " ".join(ticket_line_inserts)
ticket_line_numbers_sql = " ".join(ticket_line_numbers_inserts)

print(ticket_line_sql)
print(ticket_line_numbers_sql)

