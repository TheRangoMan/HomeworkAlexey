numbers = [str((x+1)*2) for x in range(0,10,2) if x > 5]

print((numbers))
print("".join(numbers))


dict = {'abc': 1, 'bcd': 3, 'cde': 5}
print({k.upper(): v**2 for (k, v) in dict.items()})