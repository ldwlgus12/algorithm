n = int(input())
nums = []

for i in range(n):
    lst = list(map(int, input().split()))
    nums.append(lst)
    
def pooling(size, x, y):
    mid = size//2
    
    if size == 2:
        result = [nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        result.sort()
        return result[-2]
    
    lt = pooling(mid, x, y)
    rt = pooling(mid, x+mid, y)
    lb = pooling(mid, x, y+mid)
    rb = pooling(mid, x+mid, y+mid)
    result = [lt, rt, lb, rb]
    result.sort()
    return result[-2]

print(pooling(n, 0, 0))