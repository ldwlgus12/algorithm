n, k = map(int, input().split()) 
coin = list()
cnt = 0

for i in range(n):
    coin.append(int(input()))

for j in reversed(range(n)):
    cnt += k // coin[j]
    k = k % coin[j]

print(cnt)