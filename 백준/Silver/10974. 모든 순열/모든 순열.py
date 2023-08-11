n = int(input())
nl = []

def dfs():
    if len(nl) == n:
        print(*nl)
        return
    
    for i in range(1, n+1):
        if i not in nl:
            nl.append(i)
            dfs()
            nl.pop()
            
dfs()
