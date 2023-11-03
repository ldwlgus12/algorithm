n = int(input())
stack = []
result = []
a = 0
cnt = 1

for i in range(n):
    num = int(input())
    
    while cnt <= num:       
        stack.append(cnt)
        result.append("+")
        cnt += 1

    if stack[-1] == num:    
        stack.pop()         
        result.append("-")
    else:                   
        print("NO")         
        a = 1            
        break               

if a == 0:
    for j in result:
        print(j)
        