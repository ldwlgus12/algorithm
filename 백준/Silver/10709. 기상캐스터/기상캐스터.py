h, w = map(int, input().split())
sky = [input() for _ in range(h)]
result = [[0] * w for _ in range(h)]
 
for i in range(h):
    cnt = 1
    cloud = False
    
    for j in range(w):
        if not cloud and sky[i][j] == '.':
            result[i][j] = -1
        elif sky[i][j] == 'c':
            cloud = True
            result[i][j] = 0
            cnt = 1
        elif cloud and sky[i][j] == '.':
            result[i][j] = cnt
            cnt += 1
 
for i in result:
    print(*i, end=' ')
    