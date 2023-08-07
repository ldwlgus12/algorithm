import sys
n = int(input())

tp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+tp[i][0], n+1):
        if dp[j] < dp[i] + tp[i][1]:
            dp[j] = dp[i] + tp[i][1]
                
print(dp[-1])
