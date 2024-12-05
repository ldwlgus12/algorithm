n = int(input())
lst = [[], [], []]
score = [0] * n

for i in range(n):
    nums = list(map(int, input().split()))
    lst[0].append(nums[0])
    lst[1].append(nums[1])
    lst[2].append(nums[2])
    
for i in range(3):
    for j in range(n):
        if lst[i].count(lst[i][j]) > 1:
            score[j] += 0
        else:
            score[j] += lst[i][j]
            
for i in score:
    print(i)
    