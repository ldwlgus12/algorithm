import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
result = 0

for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))

    result += x * y
    
print(result)