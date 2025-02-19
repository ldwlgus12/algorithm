n = int(input())
x = list(map(int, input().split()))

nums = [] 
nums.append(x[0])

for i in range(1, n):
    nums.append(nums[i-1] + x[i])

result = 0
for i in range(n):
    result += x[i] * (nums[n-1] - nums[i])

print(result)
