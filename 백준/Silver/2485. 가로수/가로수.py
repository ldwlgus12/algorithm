import sys, math
input = sys.stdin.readline

n = int(input())
a = int(input())
lst = []
result = 0

for i in range(n-1):
    num = int(input())
    lst.append(num - a)
    a = num

b = lst[0]

for i in range(1, len(lst)):
    b = math.gcd(b, lst[i])

for i in lst:
    result += i // b - 1
    
print(result)
