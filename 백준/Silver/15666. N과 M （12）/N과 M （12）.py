n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = []

def dfs(start):
    if len(lst) == m:
        print(*lst)
        return
    cnt = 0
    
    for i in range(start, n):
        if cnt != nums[i]:
            lst.append(nums[i])
            cnt = nums[i]
            dfs(i)
            lst.pop()

dfs(0)
