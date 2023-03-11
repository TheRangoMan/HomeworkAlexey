# Сохраните фразу на кириллице в разных кодировках
# п таблице параметров попробуйте открыть файл разными способами utf-8 koi8_r cp1251 


phrase = "Привет, мир!"


with open("utf8.txt", "w", encoding="utf-8") as f:
    f.write(phrase)

print(phrase)

with open("win1251.txt", "w", encoding="cp1251") as f:
    f.write(phrase)
print(phrase)

with open("koi8r.txt", "w", encoding="koi8_r") as f:
    f.write(phrase)
print(phrase)