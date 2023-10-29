import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    a = 5
    
    while a <= n:
        cnt += n//a 
        a *= 5
        
    print(cnt)