word = input()
a = ''

for i in word:
    if i in 'ABC':
        a += chr(ord(i) +23)
    else:
        a += chr(ord(i) - 3)
        
print(a)