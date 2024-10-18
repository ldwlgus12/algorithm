import sys
input = sys.stdin.readline

n = int(input())
line = []
result = 0

for i in range (n):
    line.append(tuple(map(int, input().split())))

line.sort()
start, end = line[0]

for i in range(1, n):
    x, y = line[i]

    if x <= end:
        end = max(y, end)
    else:
        result += (end - start)
        start, end = x, y
    
result += (end - start)
print(result)
