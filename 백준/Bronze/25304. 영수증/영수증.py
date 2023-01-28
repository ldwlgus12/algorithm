cost = int(input())
N = int(input())
result = 0

for i in range(N):
    A, B = map(int, input().split())
    money = A*B
    result += money

if cost == result:
    print('Yes')
else:
    print('No')