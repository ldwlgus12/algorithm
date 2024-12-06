n = int(input())
a = 10

while n > a:
    if n%a >= a//2:
        n += a
    n -= (n%a)
    a *= 10
    
print(n)
