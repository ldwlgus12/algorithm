h, y = map(int, input().split())
dp = [0 for _ in range(y+1)]
dp[0] = h

for i in range(1, y+1):
	if i >= 5:
		dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35))
	elif i >= 3:
		dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.2))
	else:
		dp[i] = int(dp[i-1]*1.05)

print(dp[y])
