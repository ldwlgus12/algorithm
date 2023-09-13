import sys
n, m = map(int, sys.stdin.readline().split())
p = [int(sys.stdin.readline()) for _ in range(m)]
p.sort()
price = 0
result = 0

for i in range(m):
    egg = min(m - i, n)

    if result < p[i] * egg:
        result = p[i] * egg
        price = p[i]

print(price, result)
