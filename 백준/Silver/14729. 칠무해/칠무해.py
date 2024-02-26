import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(float(sys.stdin.readline()))
lst.sort()

for i in range(7):
    print("{:.3f}".format(lst[i]))