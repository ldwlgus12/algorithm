n, m = map(int, input().split())
basket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[i:j+1] = reversed(basket[i:j+1])

basket.remove(basket[0])
print(*basket)