import sys
n = int(sys.stdin.readline().rstrip())

def Round(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n == 0:
    print(0)
else:
    lst = []    
    for i in range(n):
        lst.append(int(sys.stdin.readline().rstrip()))
        
    lst.sort()
    a = Round(n * 0.15)
    
    print(Round(sum(lst[a:n - a]) / len(lst[a:n - a])))
    