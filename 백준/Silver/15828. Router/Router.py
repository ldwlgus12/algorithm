import sys
from collections import deque 

n = int(sys.stdin.readline ())
queue = deque()
 
while True:
    a = int(sys.stdin.readline ())
        
    if a == -1:
        break
    
    if a == 0:
        queue.popleft()
    elif len(queue) < n:
        queue.append(a)
 
if queue:
    print(*queue)
else:
    print('empty')
    