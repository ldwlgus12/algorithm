import sys
input = sys.stdin.readline

n = int(input())
words = [input() for _ in range(n)]
result = True

for i in range(n):
    for j in range(n):
        if words[i][j] != words[j][i]:
            result = False
            break
    if not result:
        break

print("YES" if result else "NO")
