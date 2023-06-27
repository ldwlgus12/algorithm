chess = []
result = 0
for i in range(8):
    a = list(input())
    chess.append(a)

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if chess[i][j] == 'F':
                result += 1

print(result)