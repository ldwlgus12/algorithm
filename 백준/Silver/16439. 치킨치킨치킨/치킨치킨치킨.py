import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
chick = [list(map(int, input().split())) for _ in range(n)]
result = 0

for a, b, c in combinations(range(m), 3):
    chick_sum = 0
    
    for i in range(n):
        chick_sum += max(chick[i][a], chick[i][b], chick[i][c])
    result = max(result, chick_sum)

print(result)

