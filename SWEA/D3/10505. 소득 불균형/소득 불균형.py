T = int(input())

for i in range(1, T+1):
    T_t = int(input())
    num = list(map(int, input().split()))
    people = 0

    average = (sum(num)/T_t)
    
    for j in range(T_t):

        if num[j] <= average:
            people += 1
            
    print(f'#{i} {people}')
    