import sys
input = sys.stdin.readline
drc = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break

    board = [list(input().rstrip()) for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                continue

            cnt = 0
            for a, b in drc:
                dx, dy = i+a, j+b
                if dx >= r or dx < 0 or dy >= c or dy < 0:
                    continue

                if board[dx][dy] == '*':
                    cnt += 1

            board[i][j] = str(cnt)

    for i in board:
        print(''.join(i))
        