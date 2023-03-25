import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []
x, y = 0, 0

for _ in range(n):
    li.append(input())

for i in range(n):
    if 'X' not in li[i]:
        x += 1

for j in range(m):
    if 'X' not in [li[i][j] for i in range(n)]:
        y += 1

print(max(x, y))