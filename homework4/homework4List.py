# Сохранить в файл список из 100000 чисел
# закрыть файл
# теперь к числам этого файла постараться применить reduce
# x+y

from functools import reduce


numbers = [ x for x in range(1,10_001)]

with open("numbers.txt","w",) as file:
        file.write(str(numbers))
    

red = reduce(lambda x,y: x+y,numbers)

print(red)


