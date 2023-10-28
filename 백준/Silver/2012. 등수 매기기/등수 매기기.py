import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
result = 0

for j in range(1, n+1):
    result += abs(j-lst[j-1])
    
print(result)