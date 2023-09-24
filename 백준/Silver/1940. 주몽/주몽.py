import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

start, end = 0, len(num) - 1
cnt = 0

while start < end:
    sum = num[start] + num[end]
    
    if sum < m:
        start += 1
    elif sum > m:
        end -= 1
    else:
        start += 1
        end -= 1
        cnt += 1

print(cnt)
