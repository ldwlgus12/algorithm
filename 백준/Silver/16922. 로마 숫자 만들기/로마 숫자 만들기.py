def dfs(depth, start):
    global cnt
    if depth == n:
        nums[cnt] = 1
        return
 
 
    for i in range(start, 4):
        cnt += lst[i]
        dfs(depth + 1, i)
        cnt -= lst[i]
 
 
n = int(input())
lst = [1, 5, 10, 50]
nums = [0] * (50 * 20 + 1)
cnt = 0
dfs(0, 0)

print(sum(nums))
