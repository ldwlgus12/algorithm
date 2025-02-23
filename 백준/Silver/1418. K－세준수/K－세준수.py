import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

nums = [0 for i in range(n+1)]
result = 0

for i in range(2, n+1):
    if nums[i] == 0:
        for j in range(i, n+1, i):
            if j%i == 0:
                nums[j] = max(nums[j], i)

for i in nums:
    if i <= k:
        result += 1
        
print(result-1)
