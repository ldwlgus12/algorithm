from collections import deque
t = int(input())

for i in range(t):
    n = int(input())
    card = input().split()
    
    queue = deque()
    queue.append(card[0])
    a = card[0]
    
    for j in range(1, len(card)):
        if a >= card[j]:
            queue.appendleft(card[j])
            a = card[j]
        else:
            queue.append(card[j])
            
    print(''.join(queue))
    