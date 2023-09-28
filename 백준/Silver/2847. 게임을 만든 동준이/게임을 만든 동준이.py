n = int(input())
score = []
cnt = 0

for i in range(n):
    score.append(int(input()))

for j in range(n-2, -1, -1):
    if score[j] >= score[j+1]:
        cnt += score[j] - score[j+1] + 1
        score[j] = score[j+1] - 1

print(cnt)
