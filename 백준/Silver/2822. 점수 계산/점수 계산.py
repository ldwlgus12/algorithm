import sys
nums = []
index = []

for i in range(8):
    nums.append(int(sys.stdin.readline()))

result = sorted(nums, reverse=True)

for j in result[:5]:
    index.append(nums.index(j)+1)

index.sort()
print(sum(result[:5]))
print(*index)