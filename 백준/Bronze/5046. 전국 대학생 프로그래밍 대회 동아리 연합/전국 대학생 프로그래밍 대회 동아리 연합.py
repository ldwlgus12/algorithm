n, b, h, w = map(int, input().split())
price = []

for _ in range(h):
    p = int(input())
    a = list(map(int, input().split()))
    
    if max(a) >= n and b >= p*n:
        price.append(p*n)

if len(price) == 0:
    print("stay home")
else:
    print(min(price))
    