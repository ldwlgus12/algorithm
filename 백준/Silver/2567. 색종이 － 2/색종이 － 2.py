n = int(input())
lst = [[False for _ in range(101)] for _ in range(101)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0 

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10): 
        for k in range(y, y+10): 
            lst[k][j] = True 

for i in range(101):  
    for j in range(101):
        if lst[j][i] == True: 
            d = 0
            for k in range(4):
                if lst[j+dy[k]][i+dx[k]] == True:
                    d += 1
            if d == 3: 
                cnt += 1
            elif d == 2: 
                cnt += 2

print(cnt)
