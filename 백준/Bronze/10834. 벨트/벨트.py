import sys
input = sys.stdin.readline

m = int(input())
r = 0
result = 1

for i in range(m):
    a, b, s = map(int, input().split())
    
    if s == 1:
        r = (r+1) % 2
        
    result = (result*b) / a
    
print(r, int(result))
