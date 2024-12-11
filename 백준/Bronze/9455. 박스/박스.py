for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]    
    cnt = 0

    for i in range(n):
        bottom = m - 1
    
        for j in reversed(range(m)):
            if grid[j][i] == 1:
                cnt += bottom - j
                bottom -= 1
                  
    print(cnt)
    