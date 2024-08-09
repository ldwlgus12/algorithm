import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def star(a):
    if a == 1:
        return ['*']

    Stars = star(a//3) 
    lst = []  
   
    for i in Stars:
        lst.append(i*3)
        
    for i in Stars:
        lst.append(i + ' ' * (a//3) + i)
        
    for i in Stars:
        lst.append(i*3)
        
    return lst

n = int(input().strip())
print('\n'.join(star(n)))
