import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([i for i in range(1, n+1)])
t = 1

for i in range(n-1):
    num = (t**3) % len(queue)
    
    if num == 1:
        queue.popleft()
    else:    
        queue.rotate(-(num-1))            
        queue.popleft() 
    t += 1
    
print(*queue)
