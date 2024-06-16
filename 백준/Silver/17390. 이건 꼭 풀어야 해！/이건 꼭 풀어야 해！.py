import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

for i in range(1, len(a)):
    a[i] = a[i] + a[i-1]
    
for i in range(q):
    l, r = map(int, input().split())
    
    if l == 1:
        print(a[r-1])
    else:
        print(a[r-1] - a[l-2])
        