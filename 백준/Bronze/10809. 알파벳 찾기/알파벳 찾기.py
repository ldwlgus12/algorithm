string = input()
alpha = list(range(97, 123))

for i in alpha:
    print(string.find(chr(i)), end=" ")