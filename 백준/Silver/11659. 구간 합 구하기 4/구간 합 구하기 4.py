import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ns = list(map(int, input().split()))
nlist = [0]
hap = 0

for i in range(n):
    hap += ns[i]
    nlist.append(hap)
for j in range(m):
    a, b = map(int, input().split())
    print(nlist[b] - nlist[a-1])