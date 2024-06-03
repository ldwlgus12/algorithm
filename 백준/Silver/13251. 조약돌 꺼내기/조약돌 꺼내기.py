import sys
import math
input = sys.stdin.readline

m = int(input())
stone = list(map(int, input().split()))
k = int(input())

sum_stone = sum(stone)
same = math.comb(sum_stone, k)
result = 0

for i in stone:
    result += math.comb(i, k)

print(result/same)
