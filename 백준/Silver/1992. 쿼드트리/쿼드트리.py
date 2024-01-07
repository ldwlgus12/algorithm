n = int(input())
lst = [list(map(int, input())) for _ in range(n)]

def tree(x, y, n):
    check = lst[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != lst[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        tree(x, y, n) 
        tree(x, y+n, n)
        tree(x+n, y, n)
        tree(x+n, y+n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

tree(0, 0, n)