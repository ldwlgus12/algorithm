import sys

for i in range(3):
    s = 0
    for j in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        s += n
    
    if s == 0:
        print(0)
    elif s < 0:
        print('-')
    else:
        print('+')
