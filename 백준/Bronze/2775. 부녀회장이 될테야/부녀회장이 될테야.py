t = int(input())

for _ in range(t):  
    k = int(input()) 
    n = int(input())
    lst = [i for i in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            lst[j] += lst[j-1]
            
    print(lst[-1])