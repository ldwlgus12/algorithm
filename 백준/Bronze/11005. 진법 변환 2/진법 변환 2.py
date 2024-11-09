n, b = map(int, input().split())
result = ''
a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n != 0:
    result = a[n % b] + result
    n //= b

print(result)
