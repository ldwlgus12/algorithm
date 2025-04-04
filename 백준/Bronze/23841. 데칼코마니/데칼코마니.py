import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if paper[i][j] != ".":
            paper[i][m-j-1] = paper[i][j]

for i in paper:
    print("".join(i))
    