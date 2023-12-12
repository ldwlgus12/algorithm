t = int(input())

for i in range(t):
    string = input()
    left = []
    right = []
    
    for j in string:
        if j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        elif j == '-':
            if left:
                left.pop()
        else:
            left.append(j)
    left.extend(reversed(right))
    
    print(''.join(left))