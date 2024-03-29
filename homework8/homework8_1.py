"""
1 попробуйте сделать textdata на циклах
2 сделайте createresult на dictionaty comprehension
[ x for x in range(9)]
[ x: x+2 for x in range(9) ]
3 обработка исключений!
    там где могут быть ошибки exception мы их обрабатываем и в класс добавляем параметры
    errorFlag (True|False)
    errorMessage (str - расшифровка ошибки)
"""




#попробуйте сделать textdata на циклах

from itertools import groupby


class Textdata():
    
    def __init__(self) -> None:
        self.data=[]
        self.map = {}
        self.calendar={
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JLY": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        
    def readfile(self,filename):
        try:
            with open(filename, "r") as file:
                for line in file.readlines():
                    l = []
                    for word in line.split():
                        l.append(''.join(filter(lambda q: q.isalnum(), word)))
                    self.data.append(l)
            self.data.sort(key=lambda x: x[2])
        except:
            print('file not found!')
        return self
    
    def createresult(self):
        self.map = dict(
            map(
                lambda y: ( int(y[0]), 
                           {t[1]: int(t[0]) for t in self.sortmonths(list(y[1]))}
                           ),
                groupby(self.data, key = lambda t: t[2])
            )
        )
        return self
    
     
    def sortmonths(self,l):
         n = len(l)
         for i in range(n):
            for j in range(0,n-i-1):
                if self.calendar[l[j][1]] > self.calendar[l[j+1][1]]:
                    l[j], l[j+1] = l[j+1], l[j]
         return n


t = Textdata().readfile('HomeworkAlexey\\homework8\\input.txt').createresult()

print(t.sortmonths)
 
