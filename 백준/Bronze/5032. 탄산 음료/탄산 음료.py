e, f, c = map(int, input().split())
e += f
result = 0

while e >= c:
    a, b = e//c, e%c
    e = a+b
    result += a

print(result)