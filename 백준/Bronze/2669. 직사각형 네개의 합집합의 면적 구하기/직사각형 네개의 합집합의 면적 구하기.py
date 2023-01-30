matrix = [[0]*100 for _ in range(100+1)]
result = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for a in range(x1, x2):
        for b in range(y1, y2):
            if matrix[a][b] == 0:
                matrix[a][b] += 1

                result += 1
    
print(result)