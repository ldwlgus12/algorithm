import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    x = int(sys.stdin.readline())
    m.append(x)
m = sorted(m)

for j in range(n):
    print(m[j])