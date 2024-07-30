n, m = map(int, input().split())
board = []
cnt = []

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        color1 = 0
        color2 = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        color1 += 1
                    if board[a][b] != 'B':
                        color2 += 1
                else:
                    if board[a][b] != 'B':
                        color1 += 1
                    if board[a][b] != 'W':
                        color2 += 1
                        
        cnt.append(min(color1, color2))

print(min(cnt))
