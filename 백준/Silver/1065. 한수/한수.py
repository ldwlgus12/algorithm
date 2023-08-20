num = int(input())
hansu = 0

for n in range(1, num + 1) :
    if n <= 99 :
        hansu += 1 
    
    else :     
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2] :
            hansu += 1
            
print(hansu)