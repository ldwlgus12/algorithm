import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1):
    idx = a.index(max(a[:i+1]))
    
    if idx != i:
        a[idx], a[i] = a[i], a[idx]
        cnt += 1
        
        if cnt == k:
            print(a[idx], a[i])
            exit()
            
print(-1)
