n = int(input())
milk = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if milk[i] == cnt % 3:
        cnt += 1

print(cnt)