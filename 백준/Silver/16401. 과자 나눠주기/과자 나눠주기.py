import sys
m, n  = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 1
end = int(1e9)
result = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0
    
    for i in lst:
        cnt += i//mid
        
    if cnt >=m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
        
print(result)