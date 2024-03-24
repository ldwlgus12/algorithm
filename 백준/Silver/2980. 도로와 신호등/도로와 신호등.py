import sys
input = sys.stdin.readline

n, l = map(int, input().split())
loc = 0
result = 0

for i in range(n):
    d, r, g = map(int, input().split())
    result += (d - loc)
    loc = d
    
    if result % (r + g) <= r:
        result += (r - (result % (r + g)))

result += (l - loc)
print(result)
