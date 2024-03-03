import sys
x = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().strip().split()))
y.sort()

for i in y:
    print(i, end=' ')