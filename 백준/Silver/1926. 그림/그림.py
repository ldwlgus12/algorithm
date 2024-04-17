n, m = map(int, input().split())
art = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    art[x][y] = 0
    w = 1
    lst = list()
    lst.append([x, y])
    
    while lst:
        x, y = lst.pop()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and art[nx][ny] == 1:
                    lst.append([nx, ny])
                    art[nx][ny] = 0
                    w += 1
    return w

cnt = 0
reuslt = 0

for i in range(n):
    for j in range(m):
        if art[i][j] == 1:
            cnt += 1
            reuslt = max(dfs(i, j), reuslt)

print(cnt)
print(reuslt)
