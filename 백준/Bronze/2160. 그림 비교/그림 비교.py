import sys
input = sys.stdin.readline

n = int(input())
pics = []
lst = []

for i in range(n):
    pics.append(list([input().rstrip() for _ in range(5)]))

for i in range(n-1):
    for j in range(i+1, n):
        cnt = 0
        for a in range(5):
            for b in range(7):
                if pics[i][a][b] != pics[j][a][b]:
                    cnt += 1
        lst.append((cnt, i+1, j+1))

result = min(lst)
print(result[1], result[2])
