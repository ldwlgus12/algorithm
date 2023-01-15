chess = [1, 1, 2, 2, 2, 8]
num = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - num[i], end=" ")