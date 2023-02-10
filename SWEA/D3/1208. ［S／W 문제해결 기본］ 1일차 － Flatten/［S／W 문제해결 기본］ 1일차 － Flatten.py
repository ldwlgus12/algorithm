for i in range(1, 11):
    T = int(input())
    n = list(map(int, input().split()))


    for a in range(T):
        m = []
        ma = n.index(max(n))
        mi = n.index(min(n))

        if ma < mi:
            m.append(n.pop(ma))
            m.append(n.pop(mi-1))
        else:
            m.append(n.pop(ma))
            m.append(n.pop(mi))

        m = sorted(m)
        m[0] = m[0] + 1
        m[1] = m[1] - 1

        n.append(m[0])
        n.append(m[1])
        
        
    print(f'#{i}', max(n)-min(n))
    