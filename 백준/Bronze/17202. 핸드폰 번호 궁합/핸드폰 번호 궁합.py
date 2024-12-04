a = list(input())
b = list(input())

lst = []
result = ''
 
for i in range(8):
    result += a[i] + b[i]
 
while len(result) != 2:
    for i in range(len(result)-1):
        lst.append(str((int(result[i]) + int(result[i+1])) % 10))
        
    result = ''.join(lst)
    lst = []

print(result)
