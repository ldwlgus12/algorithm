string = input()
a, b = 0, 0

for i in range(len(string)-2):
    result = ''
    result += string[i] + string[i+1] + string[i+2]
    
    if result == 'JOI':
        a += 1
    if result == 'IOI':
        b += 1
        
print(a)
print(b)
