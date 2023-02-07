n = int(input())
for i in range(n):
    num = input()
    if len(num) >= 6 and len(num) <= 9:
        print('yes')
    else:
        print('no')