import sys
n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())

start = 1
end = m
dis = 0

for i in range(j):
    l = int(sys.stdin.readline())

    if l < start:
        dis += (start - l)
        start = l
        end = l + m - 1

    elif l > end:
        dis += (l - end)
        end = l
        start = end - m + 1

print(dis)