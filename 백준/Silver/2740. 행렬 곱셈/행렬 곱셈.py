n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

lst = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        cnt = 0
        for l in range(m):
            cnt += a[i][l] * b[l][j]
        lst[i][j] = cnt

for i in lst:
    print(*i)
    