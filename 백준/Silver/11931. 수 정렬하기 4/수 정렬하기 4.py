import sys
n = int(sys.stdin.readline())
lst = []

for i in range(0, n):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

for i in lst:
    print(i)