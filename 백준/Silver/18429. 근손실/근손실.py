n, k = map(int, input().split())
lst = list(map(int, input().split()))
check = [0]*n
cnt = 0

def dfs(day, t):
    global cnt
    
    if day == n:
        cnt += 1
        return ;
    
    for i in range(n):
        if check[i] or t+lst[i]-k < 0:
            continue            
        check[i] = 1
        dfs(day+1, t+lst[i]-k)
        check[i] = 0
        
dfs(0, 0)        
print(cnt)
