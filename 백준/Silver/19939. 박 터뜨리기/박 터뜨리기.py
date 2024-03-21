n, k = map(int, input().split())
basket = k * (k + 1) // 2

if n < basket:
    print(-1)
elif (n - basket) % k == 0:
    print(k-1)
else:
    print(k)
    