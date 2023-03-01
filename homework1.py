"""
есть строка

"зима 32нео крестьянин торжествуя 42на на"
l = []
split разбивает строку по словам
for word in phrase:
    good = True
    for letter in word:
        if not letter.isalpha():
           good = False
    if good:
        l.append(word)
"""    

p = "зима 32нео крестьянин торжествуя 42на на"

s = list(p)

phrase = ''.join(i for i in s if i.isalpha() or i ==" ")

print(phrase)


   