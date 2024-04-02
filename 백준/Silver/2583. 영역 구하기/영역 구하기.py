from collections import deque
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
result = []

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                cnt += 1
                
    return cnt

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] += 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] += 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
