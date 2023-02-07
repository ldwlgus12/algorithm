import sys
input = sys.stdin.readline

delta = { # 상하좌우, 대각선 설정
    "R": (0, 1),
    "L": (0, -1),
    "B": (-1, 0),
    "T": (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

king, stone, n = input().split() # 킹과 돌의 위치, 움직이는 회수 입력
board = [[0] * 9 for _ in range(9)] # 1~8 범위의 체스판을 위해 9*9 보드를 생성


king_r = int(king[1]) # 킹의 x 설정
king_c = ord(king[0]) - 64 # 킹의 y 설정(아스키코드 변환)
stone_r = int(stone[1]) # 돌의 x 설정
stone_c = ord(stone[0]) - 64 # 돌의 y 설정(아스키코드 변환)

for _ in range(int(n)): # 움직이는 회수 n, n번 반복
    move = delta[input().strip()] # move는 delta의 값 중 하나

    if 0 < king_r + move[0] < 9 and 0 < king_c + move[1] < 9: # 만약 킹의 x, y가 체스판의 범위를 벗어나지 않을 경우, 
        king_r += move[0] # 킹 x + 입력받은 delta 값의 범위 첫 번째(x값) 
        king_c += move[1] # 킹 y + 입력받은 delta 값의 범위 두 번째(y값)

    if king_r == stone_r and king_c == stone_c: # 만약 킹의 이동으로 킹과 돌의 위치가 같아진다면
        if 0 < stone_r + move[0] < 9 and 0 < stone_c + move[1] < 9: # 또한 돌의 x, y가 체스판의 범위를 벗어나지 않는다면,
            stone_r += move[0] # 돌 x + 입력받은 delta 값의 범위 첫 번째(x값) 
            stone_c += move[1] # 돌 y + 입력받은 delta 값의 범위 두 번째(y값)
        else: # 그게 아니라 체스판의 범위를 벗어난다면,
            king_r -= move[0]   # 킹 x 위치 이전의 자리로 이동
            king_c -= move[1]   # 킹 y 위치 이전의 자리로 이동
        
print(chr(king_c+64)+str(king_r)) # 킹의 마지막 위치 출력
print(chr(stone_c+64)+str(stone_r)) # 돌의 마지막 위치 출력
