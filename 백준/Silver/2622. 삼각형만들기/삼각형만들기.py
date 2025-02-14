import sys
input = sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        a = n-i-j
        
        if a >= i+j:
            continue
        else:				
            if j > a:
                break
            result += 1
            
print(result)
