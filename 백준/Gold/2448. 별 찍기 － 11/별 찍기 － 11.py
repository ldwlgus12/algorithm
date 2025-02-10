n = int(input())
star = [[' ']*2*n for _ in range(n)]

def recursion(x, y, n):
    if n == 3:
        star[x][y] = '*'
        star[x+1][y-1] = star[x+1][y+1] = '*'
        
        for i in range(-2, 3):
            star[x+2][y+i] = '*'
            
    else:
        N = n // 2
        recursion(x, y, N)
        recursion(x+N, y-N, N)
        recursion(x+N, y+N, N)

recursion(0, n-1, n)

for i in star:
    print("".join(i))
    