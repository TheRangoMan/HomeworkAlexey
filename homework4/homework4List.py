# Сохранить в файл список из 100000 чисел
# закрыть файл
# теперь к числам этого файла постараться применить reduce
# x+y

from functools import reduce


newlist = (list([x for x in range(1,10_001)]))

#with open("newlist.txt","w") as file:
 #   file.write(newlist)
    

red = reduce(lambda x,y: x+y,newlist)

print(red)