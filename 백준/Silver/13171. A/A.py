a = int(input())
x = int(input())

A = a
num = 1000000007
result = 1

while x:
    if x & 1:
        result = (result * A) % num
        
    A = (A**2) % num
    x //= 2
    
print(result)
