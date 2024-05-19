import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.reverse()
queue = deque()

for i in range(n):
    if a[i] == 1:
        queue.appendleft(i+1)
    elif a[i] == 2:
        queue.insert(1, i+1)
    elif a[i] == 3:
        queue.append(i+1)

for i in queue:
    print(i, end = ' ')
    