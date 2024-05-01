import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = lst[0]
    
    for j in range(1, n):
        dp[j] = max(dp[j-1] + lst[j], lst[j])
        
    print(max(dp))
    