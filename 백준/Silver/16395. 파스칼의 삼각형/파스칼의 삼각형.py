n, k = map(int, input().split())
result = [[] for _ in range(n)]

for i in range(0, n):
    for j in range(0, i+1):
        if i == 0 or j == 0 or i == j:
            result[i].append(1)
        else:
            result[i].append(result[i-1][j-1] + result[i-1][j])

print(result[n-1][k-1])
