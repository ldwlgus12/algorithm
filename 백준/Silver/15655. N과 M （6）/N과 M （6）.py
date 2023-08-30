n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
lst = []

def dfs(s):
    if len(lst) == m:
        print(*lst)
        return
    
    for i in range(s, n):
        if num[i] not in lst:
            lst.append(num[i])
            dfs(i + 1)
            lst.pop()

dfs(0)