import random
from mysql.connector import cursor
import mysql.connector



mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
# (1, 1, 23), (1, 1, 41), (1, 1, 12), (1, 1, 9), (1, 1, 32)
#
#
query = "insert into db2064.tickets (ticket_line, tickets_line_number) values "
n = 0
notfirst = False
for id in range(9000):
    for linenumber in range(5):
        for ticket_line_number in range(5):
            if notfirst:
                query += ', '
            else:
                notfirst = True
            query += f"({linenumber}, {random.randint(1,45)})"
    n += 1
    if n > 999:
        cursor.execute(query)
        mydb.commit()
        n = 0
        query = "insert into db2064.tickets (ticket_line, tickets_line_number) values "
        notfirst = False
if n != 0 :
    cursor.execute(query)
    mydb.commit()

        

mydb.commit()
mydb.close()
    
    

