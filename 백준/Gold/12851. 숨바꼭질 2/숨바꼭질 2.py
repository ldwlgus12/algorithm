import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
queue.append(n)

way = [0]*100001
cnt, result = 0, 0

while queue:
    a = queue.popleft()
    b = way[a]
    
    if a == k:
        result = b
        cnt += 1
        continue
    
    for i in [a-1, a+1, a*2]:
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a]+1):
            way[i] = way[a] + 1
            queue.append(i) 
            
print(result)
print(cnt)
