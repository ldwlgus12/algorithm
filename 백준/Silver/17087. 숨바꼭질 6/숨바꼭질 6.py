import math
n, s  = map(int, input().split())
a = list(map(int, input().split()))
lst = []

for i in a:
    lst.append(abs(s-i))

result = lst[0]

for j in range(1, n):
    result = math.gcd(lst[j], result)

print(result)