import sys
input = sys.stdin.readline

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

n = int(input())
lst = list(map(int, input().split()))
g = gcd(lst[0], gcd(lst[1], lst[-1]))

for i in range(1, g+1):
    if g%i == 0:
        print(i)