t = int(input())

for i in range(t):
    n = int(input())
    a, b = 1, 0 
    
    for j in range(n):
        a, b = b, a+b 
        
    print(a, b)
    