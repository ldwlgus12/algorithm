from heapq import *
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
    m = int(input())

    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, m)
