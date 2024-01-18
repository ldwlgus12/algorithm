import sys
n, k = map(int, sys.stdin.readline().split())
lst = []

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
    if lst[i][0] == k:
        index = i
        
for i in range(n):
    if lst[index][1:] == lst[i][1:]:
        print(i+1)
        break
