num = list(map(int, input().split()))
num.sort()

for i in num:
    if num[0] == num[1] and num[1] == num[2]:
        print(num[0])
        break
    else:
        print(num[1])
        break