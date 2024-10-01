n = list(input())
cnt = 0

for i in range(len(n)):
    cnt += int(n[i]) ** 5

print(cnt)