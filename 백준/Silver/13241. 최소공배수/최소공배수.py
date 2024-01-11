a, b = map(int, input().split())
result = a * b

while b:
    if a > b:
        a, b = b, a
    b %= a

print(result//a)