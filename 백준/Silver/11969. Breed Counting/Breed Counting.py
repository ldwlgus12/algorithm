import sys; 
input = sys.stdin.readline

n, q = map(int, input().split())
cow = [[0] * (n+1) for _ in range(3)]

for i in range(1, n+1):
    cow[int(input()) - 1][i] = 1
    
Sum = [[0] * (n + 1) for _ in range(3)]

for i in range(3):
    for j in range(1, n+1):
        Sum[i][j] = Sum[i][j - 1] + cow[i][j]

for i in range(q):
    a, b = map(int, input().split())
    
    for i in range(3):
        print(Sum[i][b] - Sum[i][a-1], end = ' ')
    print()
    