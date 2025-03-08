l = int(input())
nums = list(map(int, input().split()))
n = int(input())

nums.sort()

if n in nums:
    print(0)
else:
    Min = 0
    Max = 0
    
    for i in nums:           
        if i < n:     
            Min = i
        elif i > n and Max == 0:
            Max = i
            
    Max -= 1                 
    Min += 1
    print((n-Min) * (Max-n+1) + (Max-n))
    