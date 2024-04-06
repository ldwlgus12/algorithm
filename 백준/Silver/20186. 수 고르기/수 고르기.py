import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = 0

for i in range(1, k+1):
    result += lst[-i] - i + 1
    
print(result)