import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, now):
    for i in graph[start]:
        a, b = i
        if distance[a] == -1:
            distance[a] = now + b
            dfs(a, now+b)
            
n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [-1] * (n+5)
distance[1] = 1
dfs(1, 0)




start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))