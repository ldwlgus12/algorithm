k = int(input())
lst = []

for i in range(1, k+1):
    lst = list(map(int, input().split()))
    lst = lst[1:]
    s_lst = sorted(lst)
    cnt = 0
    
    for j in range(0, len(s_lst)-1): 
        if s_lst[j+1] - s_lst[j] > cnt:
            cnt = s_lst[j+1] - s_lst[j]
            
    print(f'Class {i}')
    print(f'Max {max(s_lst)}, Min {min(s_lst)}, Largest gap {cnt}')