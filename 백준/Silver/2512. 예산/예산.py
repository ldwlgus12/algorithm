import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(lst)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    
    for i in lst:
        if i >= mid: 
            cnt += mid 
        else: 
            cnt += i 
    if cnt <= m:
        start = mid + 1
    else: 
        end = mid - 1

print(end)