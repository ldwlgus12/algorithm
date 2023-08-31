n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
lst = []

def dfs():
    if len(lst) == m:
        print(*lst)
        return
    
    for i in range(n):
            lst.append(num[i])
            dfs()
            lst.pop()

dfs()