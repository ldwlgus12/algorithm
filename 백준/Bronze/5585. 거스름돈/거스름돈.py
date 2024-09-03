money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coins:
    cnt += money // i
    money %= i

print(cnt)