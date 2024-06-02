import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
result = []
graph = []

for i in range(h+x):
    graph.append(list(map(int, input().split())))

for i in range(h):
    result.append(graph[i][:w])

for i in range(h):
    for j in range(w):
        if i+x < h and j+y < w:
            result[i+x][j+y] -= result[i][j]

for i in result:
    print(" ".join(map(str, i)))
    