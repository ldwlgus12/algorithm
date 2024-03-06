a, b = map(int, input().split())
n = int(input())
result = abs(a-b)

for i in range(n):
    hz = int(input())
    if result > abs(hz-b):
        result = abs(hz-b) + 1

print(result)