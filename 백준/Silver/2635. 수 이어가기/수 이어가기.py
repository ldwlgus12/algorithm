n = int(input())
result = [n]

for i in range(1, n+1):
    lst = [n, i]
    while lst[-1] >= 0:
        lst.append(lst[-2] - lst[-1])
        
    lst.pop()
    if len(lst) > len(result):
        result = lst

print(len(result))
print(*result)
