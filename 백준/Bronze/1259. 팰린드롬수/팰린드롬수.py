while True:
    n = input()
    m = n[::-1]

    if n == '0':
        break
    else:
        if n == m:
            print('yes')
        else:
            print('no')
