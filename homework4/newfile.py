import sys

current_word = None # Инициализируем текущее слово как None
current_count = 0 # Инициализируем текущий счет как 0

for line in sys.stdin: # Читаем каждую строку из стандартного ввода
    word, count = line.strip().split("\t") # Удаляем пробелы и разбиваем по табуляции
    count = int(count) # Преобразуем счет в целое число

if current_word == word: # Если текущее слово совпадает с предыдущим словом
        current_count += count # Увеличиваем текущий счет на счет
else: # Если текущее слово отличается от предыдущего слова
    if current_word: # Если текущее слово не None (первая итерация)
            print(f"{current_word}\t{current_count}") # Печатаем текущее слово и его общее количество
    current_word = word # Обновляем текущее слово на новое слово
    current_count = count # Обновляем текущий счет на новый счет

if current_word == word: # Если последнее обработанное слово совпадает с предыдущим словом (последняя итерация)
    print(f"{current_word}\t{current_count}") # Печатаем последнее слово и его общее количество