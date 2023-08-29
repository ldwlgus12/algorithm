n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visit = [False] * n
result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(n):
        if not visit[i]:
            result.append(lst[i])
            visit[i] = True
            dfs()
            visit[i] = False
            result.pop()

dfs()
