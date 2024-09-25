import sys
n = int(sys.stdin.readline().rstrip())
result = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        if i*j <= n:
            result += 1
        else:
            break
            
print(result)
