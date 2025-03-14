import sys
input = sys.stdin.readline

n = int(input())
arr = [[]for _ in range(n)]
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    arr[y-1].append(x)
    
for i in arr:
    i.sort()    
    if len(i) <= 1:
        continue
        
    result += abs(i[0]-i[1]) + abs(i[-1]-i[-2])    
    for j in range(1, len(i)-1):
        result += min(abs(i[j]-i[j-1]), abs(i[j]-i[j+1]))
        
print(result)
