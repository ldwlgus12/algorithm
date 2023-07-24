n = str(input())
num = list(map(int, n))

if sum(num) % 3 == 0:
    num.sort(reverse=True)
    if num[-1] == 0:
        print(''.join(list(map(str, num))))
    else:
        print(-1)
else:
    print(-1)