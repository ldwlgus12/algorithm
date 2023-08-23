t = int(input())
dp = [1,1,1,2,2]

for i in range(5, 100):
    dp.append(dp[i-1] + dp[i-5])
 
for i in range(t):
    n = int(input())    
    print(dp[n-1])