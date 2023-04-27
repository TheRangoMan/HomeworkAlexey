import sys
from pprint import pprint
import mysql.connector
from mysql.connector import cursor
from dbHelp import DataHelp

class ChechYearandMonth:
    
    def __init__(self,year,month):
        self.year = year
        self.month = month
    
    def checkdate(self):
        if self.year < 1970 or self.year > 2050:
            return False
        if self.month < 1 or self.month > 12:
            return False
        return True


dataHelp = DataHelp()


def inputImp(question):
    p = input(question+"\t")
    if p == '.':
        print('Operation cancelled!')
        sys.exit()
    try:
        n = int(p)
    except:
        print('Please enter integer number, nothing more!')
        return(inputImp(question))
    return n

print("Hello! This is income data processing unit!")
print('You will be asked for values to enter!')
print('for exit just enter .')

while True:
    year = inputImp('Enter year:')
    month = inputImp('Enter month:')
    
    business = inputImp('Enter business:')
    income = inputImp('Enter income')
    
validator = ChechYearandMonth(year, month)


if validator.checkdate():
    print("Дата корректна.")
else:
    print("Дата некорректна.")
    
    if dataHelp.checkExist(year,month,business):
        print('We already have a record for those business and date')
        y = input('Do you want to replace existing record? input y/n')
        if y !='y':
            print("Going to next input ") 
        else:
            dataHelp.replace_data(year, month, business, income)
            print('Record updated')
    else:
        dataHelp.insert_into_query(year=year, month=month, business=business, income=income)
        print('Record created')


print(year, month, business, income)
    

