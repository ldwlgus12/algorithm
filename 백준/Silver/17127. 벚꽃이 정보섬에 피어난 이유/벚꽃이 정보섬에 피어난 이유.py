n = int(input())
a = list(map(int, input().split()))
result = 0
ires = 1

for i in range(0, n-3):
    ires *= a[i]
    jres = 1
    
    for j in range(i+1, n-2):
        jres *= a[j]
        kres = 1
        
        for k in range(j+1, n-1):
            kres *= a[k]
            lres = 1
            
            for l in range(k+1, n):
                lres *= a[l]
            result = max(result, ires+jres+kres+lres)
            
print(result)
