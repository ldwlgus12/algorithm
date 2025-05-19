p, n = map(int, input().split())
a = sorted(list(map(int, input().split())))
cnt = 0

for i in range(n):
    if p < 200:
        p += a[i]
        cnt += 1
    else:
        break

print(cnt)
