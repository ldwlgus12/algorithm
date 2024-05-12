import sys
from collections import deque
input = sys.stdin.readline

n = int(sys.stdin.readline())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

m = int(input())
c = list(map(int, input().split()))
deq = deque()

for i in range(n):
    if a[i] == 0:
        deq.appendleft(b[i])
        
for i in range(m):
    deq.append(c[i])
    print(deq.popleft(), end=' ')
    