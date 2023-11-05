import sys
n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (m + 1)] * (n + 1)
lst = []

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + lst[i-1][j-1]

print(dp[n][m])
