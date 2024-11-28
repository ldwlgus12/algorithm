a, b = input().split()
n = len(a)
m = len(b)
matrix = [['.'] * n for _ in range(m)]
 
for i in range(n):
    if a[i] in b:
        row = i
        col = b.index(a[i])
        break

for i in range(n):
    matrix[col][i] = a[i]
for i in range(m):
    matrix[i][row] = b[i]
    
for i in matrix:
    print(''.join(i))
    