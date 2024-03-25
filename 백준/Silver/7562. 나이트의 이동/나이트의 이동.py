from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    queue = deque([(x, y)])
    matrix[y][x] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == top[0] and y == top[1]:
            return matrix[y][x]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = matrix[y][x] + 1
                    queue.append([nx, ny])
                          
for i in range(t):
    l = int(input())
    under = list(map(int, input().split()))
    top = list(map(int, input().split()))
    
    matrix = [[0 for _ in range(l)] for _ in range(l)]
    print(bfs(under[0], under[1]))
    