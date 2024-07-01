from collections import deque
import sys

n, k, m = map(int, sys.stdin.readline().rstrip().split())
queue = deque();
cnt = 0

for i in range(n): 
    queue.append(i+1)
    
while queue :
    for i in range(k-1):
        queue.append(queue.popleft())        
    print(queue.popleft())
    
    cnt += 1
    
    if cnt == m: 
        queue = deque(reversed(queue));
        cnt = 0
        