def turn(d, x, y):
    global dice

    #동
    if d == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    #서
    elif d == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    #북
    elif d == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    #남
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if maps[x][y] == 0:
        maps[x][y] = dice[-1]
    else:
        dice[-1] = maps[x][y]
        maps[x][y] = 0

        
n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in cmds:
    nx = x + dx[i-1]
    ny = y + dy[i-1]

    if 0 <= nx < n and 0 <= ny < m:
        turn(i, nx, ny)
        print(dice[0])
        x, y = nx, ny
        