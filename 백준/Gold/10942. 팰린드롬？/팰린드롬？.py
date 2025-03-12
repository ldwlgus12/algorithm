import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i]=1
    
for i in range(n-1):
    if nums[i] == nums[i+1]: 
        dp[i][i+1] = 1
    else: 
        dp[i][i+1] = 0
        
for i in range(n-2):
    for j in range(n-2-i):
        k = j + 2 + i
        if nums[j] == nums[k] and dp[j+1][k-1] == 1:
            dp[j][k]=1
            
m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
    