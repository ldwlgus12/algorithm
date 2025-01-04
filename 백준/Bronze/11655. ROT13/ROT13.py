s = input()
result = ''

for i in s:
    if 'a' <= i and i <= 'z':
        i = ord(i) + 13
        if i > 122:
            i -= 26
        result += chr(i)
        
    elif 'A' <= i and i <= 'Z':
        i = ord(i) + 13
        if i > 90:
            i -= 26
        result += chr(i)
        
    else:
        result += i

print(result)
