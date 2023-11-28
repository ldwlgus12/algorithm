n = int(input())
a = list(map(int, input().split()))
nums = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

def solve(index, result, add, sub, mul, div) :
    global max_num, min_num
    
    if index >= n :
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    if add > 0 :
        solve(index+1, result+a[index], add-1, sub, mul, div)
    if sub > 0 :
        solve(index+1, result-a[index], add, sub-1, mul, div)
    if mul > 0 :
        solve(index+1, result*a[index], add, sub, mul-1, div)
    if div > 0 :
        solve(index+1, result//a[index] if result > 0 else -((-result)//a[index]), add, sub, mul, div-1)

solve(1, a[0], nums[0], nums[1], nums[2], nums[3])

print(max_num)
print(min_num)