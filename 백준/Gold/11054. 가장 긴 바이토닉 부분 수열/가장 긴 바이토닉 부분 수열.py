n = int(input())
a = list(map(int,input().split()))

rev_a = a[::-1] 
result = []

inc = [1] * n
dec = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc[i] = max(inc[i], inc[j]+1)
        
        if rev_a[i] > rev_a[j]:
            dec[i] = max(dec[i], dec[j]+1)
            
dec = dec[::-1]      
            
for i in range(n):
    result.append(dec[i] + inc[i]-1)

print(max(result))
