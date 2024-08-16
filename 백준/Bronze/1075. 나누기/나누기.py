n = int(input())
f = int(input())

a = n // 100
result = a * 100

while result % f != 0:
    result += 1
    
print(str(result)[-2:])