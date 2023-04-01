i = 0

while True:
    i += 1
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    else:
        gop = v // p
        namuji = v % p
        if l < namuji:
            namuji = l
        print(f'Case {i}: {l*gop+namuji}')