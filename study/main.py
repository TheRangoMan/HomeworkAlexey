numbers = [str((x+1)*2) for x in range(0,10,2) if x > 5]

print((numbers))
print("".join(numbers))


dict = {'abc': 1, 'bcd': 3, 'cde': 5}
print({k.upper(): v**2 for (k, v) in dict.items()})

x = "5"
try:
    total = x 
    print("Passed")
except:
    print("Language: ", end="")
else:
    print("Java")
finally:
    print("Python")
    

word = "Machine Learning"
text = word.split()
print(text)
print("".join([i[0].upper() for i in text]))

def check(word):
    if word:
        return True
    return False

words = ["home", "", "pen", None, "Nick"]

#print(list(filter(check, words)))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


print(sum(4))