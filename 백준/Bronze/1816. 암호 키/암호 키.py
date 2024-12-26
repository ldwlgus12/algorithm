n = int(input())

for _ in range(n):
    s = int(input())
    
    for i in range(2, 1000001):
        if s % i == 0:
            print("NO")
            break
            
        if i == 1000000:
            print("YES")
            