import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    a = lst[0]
    
    if a == 1:
        queue.appendleft(lst[1])
    elif a == 2:
        queue.append(lst[1])
    elif a == 3:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif a == 4:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif a == 5:
        print(len(queue))
    elif a == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a == 7:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif a == 8:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            