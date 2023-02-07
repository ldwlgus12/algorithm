while True:
    n = input()
    if n == '#':
        break
    else:
        a = n.count('a')
        A = n.count('A')
        e = n.count('e')
        E = n.count('E')
        i = n.count('i')
        I = n.count('I')
        o = n.count('o')
        O = n.count('O')
        u = n.count('u')
        U = n.count('U')
        print(a+A+e+E+i+I+o+O+u+U)