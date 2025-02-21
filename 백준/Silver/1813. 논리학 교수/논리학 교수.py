n = int(input())
nums = list(map(int, input().split()))
result = -1

for i in range(n+1):
    cnt = nums.count(i)

    if cnt == i:
        result = max(result, i)

print(result)
