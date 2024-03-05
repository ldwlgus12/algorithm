w = list(map(int, input().split()))
s = list(map(int, input().split()))
w_cnt, s_cnt = 0, 0

for i in range(9):
    w_cnt += int(w[i])
    
    if w_cnt > s_cnt:
        print("Yes")
        break
    elif i == 8 and w_cnt <= s_cnt:
        print("No")
        
    s_cnt += int(s[i])
    