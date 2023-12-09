n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
up = n * m
left = 0
front = 0

for i in range(n):
    for j in range(m):
        if j == 0:
            left += lst[i][j]
        else:
            if lst[i][j-1] < lst[i][j]:
                left += lst[i][j] - lst[i][j-1]

for j in range(m):
    for i in range(n):
        if i == 0:
            front += lst[i][j]
        else:
            if lst[i-1][j] < lst[i][j]:
                front += lst[i][j] - lst[i-1][j]
        
result = 2 * (up + left + front)
print(result)