import sys
input = sys.stdin.readline

n = int(input())
m = [0]*(n+1) 
path = ["" for _ in range(n+1)] 
path[1] = "1"

for i in range(2, n+1):
    m[i] = m[i-1] + 1
    pre = i-1
    
    if i % 3 == 0 and m[i//3] + 1 < m[i]:
        m[i] = m[i//3] + 1
        pre = i//3
        
    if i % 2 == 0 and m[i//2] + 1 < m[i]:
        m[i] = m[i//2] + 1
        pre = i//2
        
    path[i] = str(i) + " " + path[pre]

print(m[n])
print(path[n])
