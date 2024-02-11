a = 1

while True:
    n = int(input())    
    if n == 0:
        break
        
    names = [0] + [input() for _ in range(n)]
    cnt = 0
    
    for i in range(2*n-1):
        num, k = input().split()
        cnt += int(num)
        
    student = n*(n+1) - cnt
    
    print(a, names[student])
    a += 1
    