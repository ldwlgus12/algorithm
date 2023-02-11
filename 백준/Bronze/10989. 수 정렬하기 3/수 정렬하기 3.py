import sys
n = int(sys.stdin.readline())
m = [0] * 10001
for i in range(n):
    m[int(sys.stdin.readline())] += 1
for j in range(10001):
    if m[j] != 0:
        for a in range(m[j]):
            print(j)