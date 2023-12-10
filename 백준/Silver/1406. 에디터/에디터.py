import sys
left = list(input())
right = []
m = int(input())

for i in range(m):
    com = list(sys.stdin.readline().split())
    
    if com[0] == 'L' and left:
        right.append(left.pop())
    elif com[0] == 'D' and right:
        left.append(right.pop())
    elif com[0] == 'B' and left:
        left.pop()
    elif com[0] == 'P':
        left.append(com[1])

result = left + right[::-1]
print(''.join(result))
