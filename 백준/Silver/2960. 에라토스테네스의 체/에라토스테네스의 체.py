import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [False] * (n+1)
cnt = 0

for i in range(2, n+1):    
    if lst[i] == False:
        
        for j in range(i, n+1, i):            
            if lst[j] == False:
                lst[j] = True
                cnt += 1
                
                if cnt == k:
                    print(j)
                    