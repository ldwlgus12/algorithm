from collections import deque
import sys
n = int(input())
dq = deque()

for i in range(n):

    string = list(sys.stdin.readline().split( ))
    
    if string[0] == 'push_front':
        dq.appendleft(string[1])

    elif string[0] == 'push_back':
        dq.append(string[1])

    elif string[0] == 'pop_front':
        if dq:
            a = dq.popleft()
            print(a)
        else:
            print(-1)

    elif string[0] == 'pop_back':
        if dq:
            b = dq.pop()
            print(b)
        else:
            print(-1)

    elif string[0] == 'size':
        print(len(dq))


    elif string[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif string[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    
    elif string[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
 