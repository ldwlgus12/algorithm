n, k = map(int, input().split())
wheel = ['?'] * n

for i in range(k):
    spin = input().split()
    remain = int(spin[0]) % n
    s_char = str(spin[1])

    wheel = wheel[-remain:] + wheel[:-remain]	
    if wheel[0] == '?':
        if s_char in wheel:
            print('!')
            break           
        wheel[0] = s_char
        
    elif wheel[0] == s_char:
        continue
        
    else:
        print('!')
        break
        
else:
    print("".join(wheel))
    