import sys 
n, m = map(int, sys.stdin.readline().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2+1))
elif m <= 6:
    print(min(4, m))
else:
    print((2+(m-5))+1)
    