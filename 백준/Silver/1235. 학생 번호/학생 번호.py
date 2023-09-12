n = int(input())
num = []

for i in range(n):
    num.append(str(input()))
    
for j in range(1, len(num[0])+1):
    result = []
    
    for k in range(n):
        if num[k][-j:] in result:
            break
        else:
            result.append(num[k][-j:])
            
    if len(result) == n:
        print(j)
        break