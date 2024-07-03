import sys
input = sys.stdin.readline

n = int(input())
xor = 0
cnt = 0

for i in range(n):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        cnt += query[1]
        xor = xor ^ query[1]
        
    elif query[0] == 2:
        cnt -= query[1]
        xor = xor ^ query[1]
        
    elif query[0] == 3: 
        print((cnt))
        
    elif query[0] == 4: 
        print(xor)
        