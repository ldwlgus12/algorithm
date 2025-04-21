n = int(input())
a = tuple(map(int, input().split()))

check = a[0] % 2
cnt = 1

for i in a[1:]:
    if i % 2 == 1 - check:
        cnt += 1
        check = 1 - check

print(cnt)
