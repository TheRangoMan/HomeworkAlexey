from pprint import pprint
import matplotlib.pyplot as plt
from mysql.connector import cursor
import json
import mysql.connector
import numpy as nm

mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
mycursor = mydb.cursor()



fig, axs = plt.subplots(3, 1, figsize=(12, 20))

mycursor.execute("SELECT year,month,income,business FROM db2064.finances WHERE business=1 ")
result1 = mycursor.fetchall()
x1 = [m[1] for m in result1 ]
y1 = [i[2] for i in result1 ]
axs[0].plot(x1, y1, label='Бизнес 1')
axs[0].set_xlabel('Год и месяц')
axs[0].set_ylabel('Доход')
axs[0].set_title('График доходов Бизнес 1')

mycursor.execute("SELECT year,month,income,business FROM db2064.finances WHERE business=2 ")
result2 = mycursor.fetchall()
x2 = [m[1] for m in result2 ]
y2 = [i[2] for i in result2 ]
axs[1].plot(x2, y2, label='Бизнес 2')
axs[1].set_xlabel('Год и месяц')
axs[1].set_ylabel('Доход')
axs[1].set_title('График доходов Бизнес 2')

mycursor.execute("SELECT year,month,income,business FROM db2064.finances WHERE business=3 ")
result3 = mycursor.fetchall()
x3 = [m[1] for m in result3 ]
y3 = [i[2] for i in result3 ]
axs[2].plot(x3, y3, label='Бизнес 3')
axs[2].set_xlabel('Год и месяц')
axs[2].set_ylabel('Доход')
axs[2].set_title('График доходов Бизнес 3')

plt.show()

mycursor.close()
mydb.close()
