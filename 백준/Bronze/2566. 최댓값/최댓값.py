import sys
n = []
m = -1
x = 0
y = 0

for i in range(9):
    num = list(map(int, sys.stdin.readline().split()))
    n.append(num)

for a in range(len(n)):
    for b in range(len(n)):
        if m < n[a][b]:
            m = n[a][b]
            x = a + 1
            y = b + 1

print(m)
print(x, y)