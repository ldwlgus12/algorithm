a = input().split('-')
result = 0

for i in a[0].split('+'):
    result += int(i)
    
for j in a[1:]:
    for k in j.split('+'):
        result -= int(k)
        
print(result)