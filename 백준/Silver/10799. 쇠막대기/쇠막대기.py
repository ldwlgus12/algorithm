lst = list(input())
stack = []
cnt = 0

for i in range(len(lst)):    
    if lst[i] == '(':
        stack.append('(')
    else:
        if lst[i-1] == '(': 
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop() 
            cnt += 1 

print(cnt)