t = int(input())
n = list(map(int, input().split()))

lst = [0] * 80001
cnt = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        cnt += i
    lst[i] = cnt

for i in n:
    print(lst[i])
    