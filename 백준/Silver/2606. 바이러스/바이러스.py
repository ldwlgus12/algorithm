n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visit[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visit[adj]:
                visit[adj] = True
                stack.append(adj)
dfs(1)
print(sum(visit)-1)