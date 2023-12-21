import sys
n, k, b = map(int, sys.stdin.readline().split())
lst = [0 for _ in range(n+1)]

for i in range(b):
    b = int(sys.stdin.readline())
    lst[b] = 1

for i in range(1, n+1):
    lst[i] += lst[i-1]
result = b

for i in range(k, n+1):
    result = min(result, lst[i] - lst[i-k])

print(result)