M = int(input())
cup = [1,2,3]

for i in range(M):
    x, y = map(int, input().split())
    nx = cup.index(x)
    ny = cup.index(y)
    cup[nx], cup[ny] = cup[ny], cup[nx]
    
print(cup[0])