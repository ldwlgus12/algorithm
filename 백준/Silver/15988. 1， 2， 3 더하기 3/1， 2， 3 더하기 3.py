import sys
t = int(sys.stdin.readline())

dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    dp[i] = dp[i-1]%1000000009 + dp[i-2]%1000000009 + dp[i-3]%1000000009

for j in range(t):
    n = int(sys.stdin.readline())
    print(dp[n] % 1000000009)