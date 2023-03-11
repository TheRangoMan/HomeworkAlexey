# подсчитать количество уникальных слов в файле про шерлока холмса
# создать словарь - {уникальное слово: количество повторений}

#sherlockText = "C:\\Users\\Alexey\\Desktop\\Python 2.0\\HomeworkAlexey\\homework4\\advs.txt"

with open ("C:\\Users\\Alexey\\Desktop\\Python 2.0\\HomeworkAlexey\\homework4\\advs.txt", "r") as f:
    words = f.read().split()
    pass
#print(words)






'''
with open ("worldList.txt","w") as f:
     f.write(str(words))
     pass
'''


word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


#print("Количество уникальных слов:", len(word_counts))


#print("Словарь уникальных слов и количества повторений:", word_counts)



