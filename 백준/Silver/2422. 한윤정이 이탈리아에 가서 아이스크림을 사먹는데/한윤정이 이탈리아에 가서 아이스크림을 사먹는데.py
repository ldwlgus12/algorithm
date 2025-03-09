import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ic = [[False for _ in range(n)] for _ in range(n)]
result = 0

for i in range(m):
    mix1, mix2 = map(int, input().split())
    ic[mix1-1][mix2-1] = True
    ic[mix2-1][mix1-1] = True

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not ic[i][j] and not ic[i][k] and not ic[j][k]:
                result += 1

print(result)
