n = int(input())

a = 5
dot = 7

for i in range(1, n):
    a += dot
    dot += 3
    
print(a % 45678)
