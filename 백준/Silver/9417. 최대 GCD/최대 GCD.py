t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    nums.sort()  
    result = 0  
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a, b = nums[j], nums[i]  
            
            while a % b != 0: 
                a, b = b, a % b
                
            if result < b: 
                result = b

    print(result)
    