import sys
input = sys.stdin.readline
 
n, s, r = map(int, input().split())
s_num = list(map(int, input().split()))
r_num = list(map(int, input().split()))
s_num, r_num = list(set(s_num)-set(r_num)), list(set(r_num)-set(s_num))	

result = 0
for i in s_num:
    if i-1 in r_num:
        r_num.remove(i-1)
    elif i+1 in r_num:
        r_num.remove(i+1)
    else:
        result += 1

print(result)
