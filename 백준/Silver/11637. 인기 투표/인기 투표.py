t = int(input())

for i in range(t):
    n = int(input())
    lst = []
    
    for j in range(n):
        vote = int(input())
        lst.append(vote)
        
    major = int(sum(lst)/2)
    mx = max(lst)
    mx_idx = lst.index(mx) + 1
    
    if lst.count(mx) >= 2:
        print('no winner')
    else:
        if mx > major:
            print(f'majority winner {mx_idx}')
        else:
            print(f'minority winner {mx_idx}')
            