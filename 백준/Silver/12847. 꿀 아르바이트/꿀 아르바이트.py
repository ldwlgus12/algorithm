import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = list(map(int, input().split()))

step = m
sum_money = sum(money[:step])
result = sum_money

for i in range(step, n):
    sum_money += money[i] - money[i - step]
    result = max(result, sum_money)

print(result)
