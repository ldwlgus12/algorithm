n, m = map(int,input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
lst = []

for i in range(n):
    for j in range(m):
        if nums[i][j] == 1:
            if len(lst) == 0:
                lst = [i+1, j+1]
            else:
                a = [i+1, j+1]
                
print(abs(a[0]-lst[0]) + abs(a[1]-lst[1]))
