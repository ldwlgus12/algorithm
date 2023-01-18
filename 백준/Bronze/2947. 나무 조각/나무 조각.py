num = list(map(int, input().split()))
result = [1, 2, 3, 4, 5]

while(True):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(' '.join(map(str, num)))

    if num == result:
        break