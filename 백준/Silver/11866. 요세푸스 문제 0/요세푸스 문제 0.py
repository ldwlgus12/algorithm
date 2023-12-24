import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, n+1)])
result = []

while len(deq) != 0:
    for i in range(k-1):
        deq.append(deq.popleft())
    result.append(str(deq.popleft()))

print('<'+', '.join(result)+'>')