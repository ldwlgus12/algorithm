n, m = list(map(int,input().split()))
l = []

def dfs(start):
    if len(l)==m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(start, n+1):
        if i not in l:
            l.append(i)
            dfs(i+1)
            l.pop()
            
dfs(1)