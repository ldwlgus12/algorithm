import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
lst = []

for _ in range(m):
    a, b, c = map(int, input().split())
    lst.append((c, a, b))

lst.sort()
result = 0

for c, a, b in lst:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)
