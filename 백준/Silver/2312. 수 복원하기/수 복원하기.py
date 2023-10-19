t = int(input())

for i in range(t):
    n = int(input())
    lst = []
    num = 2
    
    while n != 1:
        cnt = 0
        while True:
            if n % num == 0:
                n //= num
                cnt += 1
            else:
                break
                
        lst.append([num, cnt])
        num += 1
        
    for j in lst:
        if j[1]:
            print(*j)