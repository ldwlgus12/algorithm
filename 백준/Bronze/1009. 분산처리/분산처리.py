import sys
n = int(sys.stdin.readline())

for i in range(n): 
    a,b = map(int, sys.stdin.readline().split())
    c = a%10
    
    if c == 0:
        print(10)
    elif c in [1,5,6]:
        print(c)
    elif c in [4,9]:
        d = b%2
        if d == 1:
            print(c)
        else:
            print((c * c) % 10)
    else:
        e = b % 4
        if e == 0:
            print((c**4)%10%10%10)
        else:
            print((c**e)%10%10%10)