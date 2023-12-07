import sys
s, k = map(int, sys.stdin.readline().split(" "))
n = (s//k) 
m = (s%k)
result = 1

for i in range(k):
    if m > 0:
        result *= (n+1)
        m -= 1
    else:
        result *= n
        
print(result)