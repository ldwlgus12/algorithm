import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
stiker = list(list(map(int, input().split())) for _ in range(n))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = stiker[i]
        r2, c2 = stiker[j]

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
            
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
            
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
            
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
            
print(result)
