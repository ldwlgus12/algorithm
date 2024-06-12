import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = [input().split() for _ in range(n)]
name.sort(key=lambda x: int(x[1]))
power = [int(input().strip()) for _ in range(m)]

for i in power:
    r = len(name)
    l = 0
    result = 0
    
    while l <= r:
        m = (l+r) // 2
        
        if int(name[m][1]) >= i:
            result = m
            r = m - 1
        else:
            l = m + 1
            
    print(name[result][0])
    