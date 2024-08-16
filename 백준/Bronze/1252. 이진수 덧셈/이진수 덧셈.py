a, b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)

result = a + b
print(bin(result)[2:])
