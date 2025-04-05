n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1):
    idx = lst.index(max(lst[:i+1]))
    
    if idx != i:
        lst[idx], lst[i] = lst[i], lst[idx]
        cnt += 1
        if cnt == k:
            print(*lst)
            exit()
            
print(-1)
