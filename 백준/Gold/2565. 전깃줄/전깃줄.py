import sys
input = sys.stdin.readline

n = int(input())
lst = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort()

for i in range(1, n):
  for j in range(0, i):
    if lst[j][1] < lst[i][1]:
        dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
