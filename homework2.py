# нельзя использовать циклы и условия
# Добавление любимых фраз Копатыча и Лосяша
# addPhrase(beasts, "Лосяш", "Хрю")
# print(beasts)
# Поиск серий, в которых участвуют оба персонажа
# allSeries(beasts)
# print(seriesSets(beasts))
# Удаление серии Герой Плутона из списка серий Лосяша
# l = getBeast(beasts,'Лосяш')
# l['Серии'].remove('Герой Плутона')
# print(l)
# seriesRemove(beasts, 'Лосяш', 'Герой Плутона')
# print(getBeast(beasts,'Лосяш'))
# Замена цвета Копатыча на Светло-коричневый
# l = getBeast(beasts,'Копатыч')
# l['Цвет'] = "Светло-коричневый"
# print(l)
# changeColor(beasts,"Копатыч","Светло-коричневый")
# print(getBeast(beasts,'Копатыч'))
# Добавление данных о любом другом смешарике пользователем
# addBeast(beasts)
# print(beasts)
# Подсчет количества записанных смешариков
# ???
# Создание второй структуры, идентичной первой, удаление оттуда записи про Копатыча так чтобы оригинальная структура не поменялась
# Создавайте )
# deleteBeast(omg,'Копатыч')

def getBeastByName(beasts, name):
    beast = list(filter(lambda beast: beast["Имя"] == name, beasts))[0]
    return beast

def addPhrase(beasts, name):
    if name == "Лосяш":
        beasts[0]["Фраза"] = "Хрю"
    elif name == "Копатыч":
        beasts[1]["Фраза"] = " "
    return beasts    

def seriesRemove(beasts,name):
    if name == "Лосяш":
        beasts[0]['Серии'].remove('Герой Плутона')
        return beasts


beasts = list()

beasts.append({
    "Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]
})

beasts.append({
    "Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
})
#beasts2 = beasts.copy()
#print(list(filter(lambda beast: beast["Имя"] == "Лосяш", beasts)))
#print(beasts)
#print(getBeastByName(beasts,"Лосяш"))


#print(addPhrase(beasts,"Лосяш"))

print(seriesRemove(beasts,"Лосяш"))
        