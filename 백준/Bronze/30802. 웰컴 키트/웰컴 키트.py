n = int(input())
nums = list(map(int, input().split()))
t, p = map(int, input().split())

t_num = 0
p_num = n//p
pen = n%p

for i in nums:
    if i == 0:
        continue
    elif i <= t:
        t_num += 1
    elif i%t == 0:
        t_num += i//t
    else:
        t_num += i//t+1

print(t_num)
print(f'{p_num} {pen}')
