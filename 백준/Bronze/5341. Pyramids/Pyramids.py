while True:
    try:
        hap = 0
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(n):
                hap += (n - i)
        print(hap)

    except:
        break