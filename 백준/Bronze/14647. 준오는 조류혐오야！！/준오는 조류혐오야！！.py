n, m = map(int, input().split())
lst = []
row, col = [], []

for _ in range(n):
    bingo = list(map(str, input().split()))
    lst.append(bingo)
    rowCnt = 0
    
    for i in bingo:
        rowCnt += i.count('9')
    row.append(rowCnt)

for i in range(m):
    colCnt = 0
    for j in range(n):
        colCnt += lst[j][i].count('9')
    col.append(colCnt)

print(sum(row) - max(max(row), max(col)))
