t = int(input())
for i in range(t):
    a = list(input().split())
    n = float(a.pop(0))

    for i in range(len(a)):
        if a[i] == '@':
            n *= 3
        elif a[i] == '%':
            n += 5
        elif a[i] == '#':
            n -= 7

    print('%0.2f' % n)