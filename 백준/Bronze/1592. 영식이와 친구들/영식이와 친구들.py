n, m, l = map(int, input().split())
lst = [0] * n
a, cnt = 0, 0

while True:
    lst[a%n] += 1
    
    if lst[a%n] == m:
        print(cnt)
        break
        
    cnt += 1
    a += l
