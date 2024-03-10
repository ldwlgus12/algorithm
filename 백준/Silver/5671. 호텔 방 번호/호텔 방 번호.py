import sys

while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
    except:
        break
        
    result = 0
    
    for i in range(n, m+1):
        tmp = set()
        s_i = str(i)
        for j in s_i:
            tmp.add(j)
        if len(s_i) == len(tmp):
            result += 1
            
    print(result)
    