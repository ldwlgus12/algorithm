import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start, end = 0, 1
cnt = 0

while (start <= end and end <= n):
    result = sum(lst[start:end])

    if (result < m):
        end += 1
    elif (result > m):
        start += 1
    else:
        end += 1
        cnt += 1
        
print(cnt)
