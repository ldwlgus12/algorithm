n = int(input())
graph = []

for i in range(n):
    Map = list(map(int, input().split()))
    graph.append(Map)

start = (0, 0)
visited = [[0]*n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            dfs(nx, ny)

dfs(0, 0)
if visited[n-1][n-1] == True:
    print('HaruHaru')
else:
    print('Hing')
    