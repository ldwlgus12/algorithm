n = int(input())
grid = [[0]*1001 for _ in range(1001)]

for i in range(1, n+1):
    x, y, w, h = map(int, input().split())    
    for j in range(y, y+h):
        grid[j][x:x+w] = [i]*w

result = [0]*(n+1)

for i in grid:
    for j in i:
        result[j] += 1
        
print(*result[1:], sep='\n')
