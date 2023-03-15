"""
сделайте класс WordCount
он должен получать строку содержащую текст и считать количество слов в этом тексте как было в ДЗ слово и его количество вхождений
"""

class WordCount():
    
    def __init__(self, text) -> None:
        self.text = text
        pass
    
    def count_words(self):
        words = self.text.split()
        total_count = len(words)
        unique_words = set(words)
        word_counts = {word: words.count(word) for word in unique_words}
        return total_count, word_counts
    pass



text ="To Sherlock Holmes she is always the woman."
wc = WordCount(text)
total_count, word_counts = wc.count_words()
print("Total words:", total_count)
print("Word counts:", word_counts)