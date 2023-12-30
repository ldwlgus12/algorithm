import sys
n, k = map(int, sys.stdin.readline().split())
result = 1
num = 1

for i in range(k):
    result *= n
    n -= 1

for j in range(2, k+1):
    num *= j

print((result // num) % 10007)