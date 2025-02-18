import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
benefit, result = 0, 0

for i in range(n-1, -1, -1):
    benefit = max(benefit, a[i])
    result = max(result, benefit - a[i])

print(result)
