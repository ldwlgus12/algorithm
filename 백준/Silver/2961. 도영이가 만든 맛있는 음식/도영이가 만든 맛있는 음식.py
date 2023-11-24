import sys
from itertools import combinations
n = int(sys.stdin.readline())
lst = []
food = []
result = 1000000000

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split(" "))))

for j in range(1, n+1):
    food.append(combinations(lst, j))

for i in food:
    for j in i:
        sour = 1
        bitter = 0
        for k in j:
            sour *= k[0]
            bitter += k[1]

        result = min(result, abs(sour-bitter))

print(result)