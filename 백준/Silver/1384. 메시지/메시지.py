import sys
input = sys.stdin.readline
cnt = 0

while True:
    n = int(input())
    cnt += 1
    trouble = []
    result = []
    
    if n == 0:
        break
    
    lst = [input().split() for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if lst[i][j] == "N":
                trouble.append([i, j])
    
    for x, y in trouble:
        if x >= y:
            result.append([x, x-y])
        elif x < y:
            result.append([x, n-y+x])
    print("Group", cnt)
    
    if result:
        for x, y in result:
            print(lst[y][0], "was nasty about", lst[x][0])
    else:
        print("Nobody was nasty")
    print("")
    