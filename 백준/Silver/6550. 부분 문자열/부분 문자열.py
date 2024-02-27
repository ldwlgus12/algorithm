while True:
    try:
        s, t = input().split()    
        cnt = 0
        part = 0
    
        for i in range(len(t)):
            if t[i] == s[cnt]:
                cnt += 1
            if cnt == len(s):
                part = 1
                break

        if part == 1:
            print('Yes')
        else:
            print('No')

    except:
        break