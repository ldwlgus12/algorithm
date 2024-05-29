import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
result = 0

for i in s:
	if i == '(':
		stack.append(i)
	else: 
		if stack: 
			stack.pop() 
		else: 
			result += 1
            
result += len(stack)

print(result) 
