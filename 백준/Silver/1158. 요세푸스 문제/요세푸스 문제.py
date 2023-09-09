n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
result = []
num = 0 

for i in range(n):
    num += k-1
    
    if num >= len(lst):  
        num = num % len(lst)
        
    result.append(str(lst.pop(num)))
    
print("<", ", ".join(result)[:], ">", sep='')