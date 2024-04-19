import sys
import math
input = sys.stdin.readline
n = int(input())

for i in range(n):
    lst = list(map(int, input().split()))
    result = 0
    
    for j in range(1, len(lst)):
        for k in range(j+1, len(lst)):
            result += math.gcd(lst[j], lst[k])

    print(result)
    