n = int(input())
nums = list(map(int, input().split()))

stack = []
target = 1
 
while nums:
    if nums[0] == target:
        nums.pop(0)
        target += 1
    else:
        stack.append(nums.pop(0))
 
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
 
if stack: 
    print('Sad')
else:
    print('Nice')
    