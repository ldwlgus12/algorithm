import sys
lst = []
result = 0

for i in range(int(input())):
    asim = list(map(int, sys.stdin.readline().split()))
    
    if asim[0] == 1:
        lst.append((asim[1], asim[2]))
    
    if lst:
        score, time = lst.pop()
        time -= 1
        
        if time == 0:
            result += score
        else:
            lst.append((score, time))
            
print(result)