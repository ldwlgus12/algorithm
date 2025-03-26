n = int(input())
cnt = 1
cat = 1

if n == 0:
    print(0)
else:
    while cat < n:
        cat *= 2
        cnt += 1
    print(cnt)
    