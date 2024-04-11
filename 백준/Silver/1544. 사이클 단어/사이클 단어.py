import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cycle = []

for i in range(n):
    cycle.append(input().rstrip())

for i in range(n):
    dq = deque(cycle[i])
    
    while True:
        dq.append(dq.popleft())
        a = "".join(dq)
        
        if a == cycle[i]:
            break

        if a in cycle:
            idx = cycle.index(a)
            cycle.pop(idx)
            cycle.insert(idx, cycle[i])

cycle = set(cycle)
print(len(cycle))
