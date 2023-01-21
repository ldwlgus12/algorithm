T = int(input())
length = 0
 
for i in range(1, T+1):
    num = list(map(int, input().split()))
     
    if num[0] == num[1]:
        length = num[2]
    elif num[1] == num[2]:
        length = num[0]
    elif num[0] == num[2]:
        length = num[1]
    elif num[0] == num[1] == num[2]:
        length = num[0]
     
    print(f'#{i} {length}')