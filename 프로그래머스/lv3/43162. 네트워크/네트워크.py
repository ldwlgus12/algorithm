def solution(n, computers):
    cnt = 0
    visited = [False for i in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            cnt += 1    # DFS로 최대한 많은 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크가 된다
    return cnt

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

