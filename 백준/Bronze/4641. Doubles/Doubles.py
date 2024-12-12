while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == -1:
        break
  
    result = 0
    for i in range(len(nums)-1):
        if nums[i] % 2 == 0:
            if nums[i] // 2 in nums:
                result += 1

    print(result)
    