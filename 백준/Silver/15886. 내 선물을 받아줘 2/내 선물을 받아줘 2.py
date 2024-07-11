import sys
input = sys.stdin.readline

n = int(input())
m = input()
result = 1

for i in range(1, n):
    if m[i] == 'E':
        if m[i-1] == 'W':
            result += 1
            
print(result)
