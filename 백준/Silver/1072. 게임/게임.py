import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y*100) // x

if z >= 99:
    print(-1)
else:
    result = 0
    L = 1
    R = x
    
    while L <= R:
        mid = (L+R) // 2
        
        if (y+mid) * 100 // (x+mid) <= z:
            L = mid + 1
        else:
            result = mid
            R = mid - 1
            
    print(result)