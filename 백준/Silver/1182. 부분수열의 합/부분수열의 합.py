import sys
n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = []
cnt = 0

def solve(start):
    global cnt
    
    if sum(result) == s and len(result) > 0:
        cnt += 1

    for i in range(start, n):
        result.append(lst[i])
        solve(i+1)
        result.pop()

solve(0)
print(cnt)
