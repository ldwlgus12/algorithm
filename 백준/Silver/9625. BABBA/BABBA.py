k = int(input())
a, b = 0, 1

for i in range(1, k):
    a, b = b, a+b
    
print(a, b)