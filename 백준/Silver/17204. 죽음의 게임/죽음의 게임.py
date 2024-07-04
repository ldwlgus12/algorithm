n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
p = 0
m = 0

for i in range(n):
    target = num[p]
    m += 1
    
    if target == k:
        print(m)
        break
        
    p = target
else:
    print(-1)
        