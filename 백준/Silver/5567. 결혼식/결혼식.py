import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque()
    visit[x] = 1
    queue.append(x)
    
    while queue:
        a = queue.popleft()  
        
        for j in graph[a]:
            if visit[j] == 0:
                queue.append(j)
                visit[j] = visit[a] + 1

bfs(1)
result = 0

for k in range(2, n+1):
    if visit[k] < 4 and visit[k] != 0:
        result += 1
        
print(result)