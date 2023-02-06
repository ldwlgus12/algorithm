import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

dx = [-1,0,1,0,-1,-1,1,1] # 상하좌우, 대각선 확인용
dy = [0,1,0,-1,-1,1,-1,1]

def dfs(i,j):
    for x in range(8): # 상하좌우, 대각선 확인용
        nx = i + dx[x]
        ny = j + dy[x]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            # 상하좌우, 대각선 살펴보다 육지가 있으면 0으로 바꾸기
            graph[nx][ny] = 0 # 다시 카운트 하지 않기 위해
            dfs(nx, ny)     # 육지가 있으면 그걸 기준으로 또 상하좌우, 대각선 확인

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # 입력받기
    graph = []
    result = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w): 
            if graph[i][j] == 1: # for문 돌며 육지가 발견 될 경우
                result += 1 # 하나 세고
                graph[i][j] = 0 # 다시 카운트 하지 않기 위해 0으로 바꿈
                dfs(i,j)
    print(result)