nums = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        if sum(nums) - nums[i] - nums[j] == 100:
            a, b = i, j
            break
nums.pop(a)
nums.pop(b-1)

for i in nums:
    print(i)
    