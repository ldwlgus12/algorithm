n = int(input())
lst = list(map(int, input().split()))
result = []

for i in range(n):
    a = lst[i] * (i+1)
    
    for j in range(len(result)):
        a -= result[j]
    result.append(a)
    
for i in result:
    print(i, end=' ')
    