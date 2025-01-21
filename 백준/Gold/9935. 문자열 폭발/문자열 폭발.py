import sys
s = list(sys.stdin.readline().strip())
p = list(sys.stdin.readline().strip())
lp = len(p)
stack = []

for i in s:
    stack.append(i)
    if stack[len(stack)-lp : len(stack)] == p:
        for j in range(lp):
            stack.pop()
            
if stack:
    print(*stack, sep='')
else:
    print("FRULA")
    