t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    lst = []
    cnt = 0
    
    for i in range(n):
        r, c = map(int, input().split())
        lst.append(r*c)
    lst.sort(reverse=True)
    
    while j > 0:
        j -= lst[cnt]
        cnt += 1
        
    print(cnt)