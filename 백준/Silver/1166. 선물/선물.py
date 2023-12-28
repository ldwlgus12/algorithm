import sys
n, l, w, h = map(int, sys.stdin.readline().split())
s, e = 0, max(l, w, h)

for i in range(10000):
    m = (s + e) / 2
    cnt = (l // m) * (w // m) * (h // m)
    
    if cnt >= n:
        s = m
    else:
        e = m

print("%.10f" %(m))