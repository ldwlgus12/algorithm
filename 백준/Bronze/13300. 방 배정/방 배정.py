n, k = map(int, input().split()) 
lst = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
result = 0

for i in range(n):
    s, g  = map(int, input().split())
    lst[s][g-1] += 1

for i in lst:
    for j in i:
        if j % k == 0:
            result += j//k
        else:
            result += (j//k) + 1
            
print(result)