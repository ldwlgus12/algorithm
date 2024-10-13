t = int(input())

for i in range(t):
    n = int(input())
    result = 0 
    
    for j in range(1, n):
        if j**2 <= n:
            result += 1
        if j**2 > n:
            break
            
    print(result)