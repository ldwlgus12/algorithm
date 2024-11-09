import sys
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == -1:
        break
    
    lst = []
    
    for i in range(1, n):
        if n%i == 0:
            lst.append(i)
    
    if sum(lst) == n:
        print(n, '=', end=' ')
        print(*lst, sep=' + ')
    else:
        print("%d is NOT perfect." %n)
        