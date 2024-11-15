import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())  # 도시 수
m = int(input())  # 버스 수

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    # a = 시작 도시 / b = 도착 도시 / c = 한 번 타는데 필요한 비용
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b]) 

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF:
            print("0", end=" ")
        else:
            print(graph[x][y], end=" ")     
            
    print()   
    