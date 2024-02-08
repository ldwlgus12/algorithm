import sys
n = int(input())
lst = []
i = 2

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key = lambda x: -x[2])

print(*lst[0][:2])
print(*lst[1][:2])

if lst[0][0] == lst[1][0]:
    while lst[0][0] == lst[i][0]:
        i += 1
        
print(*lst[i][:2])
