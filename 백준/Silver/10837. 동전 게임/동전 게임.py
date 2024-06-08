k = int(input())
c = int(input())
result = []

for i in range(c):
    m, n = map(int, input().split())
    
    if m < n:
        if n-m-1 >= k-n+1: 
            result.append("0")
        else: 
            result.append("1")
    elif m > n:
        if m-n-1 > k-m+1: 
            result.append("0")
        else: 
            result.append("1")
    else: 
        result.append("1")
        
for i in result: 
    print(i)
    