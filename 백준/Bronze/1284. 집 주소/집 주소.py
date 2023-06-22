while(True):
    nl = []
    n = input()
    t = 0
    l = len(n)-1
    
    if n == '0':
        break

    for i in n:
        nl.append(i)


    for i in n:
        if i == '1':
            t += 2
        elif i == '0':
            t += 4
        else:
            t += 3
    print(t+l+2)