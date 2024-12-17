import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []
result = 0

for i in range(n):
    nums = int(input())
    heapq.heappush(cards, nums)

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a + b
    heapq.heappush(cards, a+b)

print(result)
