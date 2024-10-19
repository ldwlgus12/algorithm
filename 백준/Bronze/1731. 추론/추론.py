n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))
    
result = lst[-1]

if lst[1] - lst[0] == lst[2] - lst[1]:
    result += (lst[1] - lst[0])
elif lst[1] // lst[0] == lst[2] // lst[1]:
    result *= (lst[1] // lst[0])

print(result)
