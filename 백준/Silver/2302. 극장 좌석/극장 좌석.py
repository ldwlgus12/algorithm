import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = []

for i in range(0, m):
    vip = int(input())
    lst.append(vip)
dp = [1, 1, 2]

for i in range(3, 41):
    dp.append(dp[i-2] + dp[i-1])
result = 1

if m >= 1:
    pre = 0
    
    for i in range(0, m):
        result = result * dp[lst[i] - 1 - pre]
        pre = lst[i]
    result = result * dp[n-pre]
else:
    result = dp[n]
    
print(result)
