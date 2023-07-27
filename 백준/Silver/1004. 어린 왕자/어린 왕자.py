t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0
    
    for j in range(n):
        px, py, radius = map(int, input().split())
        s = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
        e = (((px - x2) ** 2) + ((py - y2) ** 2)) ** 0.5
        
        if s < radius and e < radius:
            pass
        elif s < radius:
            result += 1
        elif e < radius:
            result += 1
    
    print(result)
    