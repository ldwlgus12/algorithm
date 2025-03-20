import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
result = 0
summ = 0

for i in range(n):
    result += nums[i] * summ
    summ += nums[i]

print(result)
