while True:
    rt = list(map(int, input().split()))

    if rt[0] == 0 and rt[1] == 0 and rt[2] == 0:
        break

    rt.sort()

    if ((rt[0]**2 + rt[1]**2) == rt[2]**2):
        print('right')
    else:
        print('wrong')