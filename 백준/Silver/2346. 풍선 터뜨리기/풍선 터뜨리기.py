import sys
from collections import deque

n = int(input())
deq = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while deq:
    idx, q = deq.popleft()
    result.append(idx + 1)

    if q > 0:
        deq.rotate(-(q - 1))
    elif q < 0:
        deq.rotate(-q)

print(' '.join(map(str, result)))
