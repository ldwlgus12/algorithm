import sys
import heapq

N = int(input())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(num_list, (abs(num), num))
    else:
        if not num_list:
            print(0)
        else:
            print(heapq.heappop(num_list)[1])