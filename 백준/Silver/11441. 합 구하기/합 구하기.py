import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
sum = [lst[0]]

for i in range(1, n):
    sum.append(sum[-1] + lst[i])

m = int(input())
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(sum[b-1])
    else:
        print(sum[b-1] - sum[a-2])