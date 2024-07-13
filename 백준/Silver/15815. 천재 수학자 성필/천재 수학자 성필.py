import sys
input = sys.stdin.readline

string = input().strip()
stack = []
result = 0

for i in string:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
        
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
        
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
        
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b//a)
        
    else:
        stack.append(int(i))

for j in stack:
    print(j)
    