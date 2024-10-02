n = int(input())
height = [int(input()) for _ in range(n)]
l_cnt, r_cnt = 0, 0
l_max, r_max = 0, 0

for i in height:
    if i > l_max:
        l_max = i
        l_cnt += 1
        
for j in height[::-1]:
    if j > r_max:
        r_max = j
        r_cnt += 1
        
print(l_cnt)
print(r_cnt)