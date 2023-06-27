n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    a, b = basket[i], basket[j]
    basket[i] = b
    basket[j] = a

basket.remove(basket[0])
print(*basket)