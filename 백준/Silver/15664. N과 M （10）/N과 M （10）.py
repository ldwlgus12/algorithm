n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visit = [False] * n
lst = []

def dfs(start):
    if len(lst) == m:
        print(*lst)
        return
    cnt = 0
    
    for i in range(start, n):
        if not visit[i] and cnt != nums[i]:
            visit[i] = True
            lst.append(nums[i])
            cnt = nums[i]
            dfs(i+1)
            visit[i] = False
            lst.pop()

dfs(0)
