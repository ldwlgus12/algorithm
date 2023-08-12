import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set()

for i in range(n):
    s.add(input())
    
result = 0

for j in range(m):
    word = input()
    if word in s:
        result += 1
        
print(result)