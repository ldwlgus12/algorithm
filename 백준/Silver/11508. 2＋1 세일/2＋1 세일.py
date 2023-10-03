import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)
result = 0

for j in range(n):
    if j % 3 != 2:
        result += lst[j]
        
print(result)