H, M = map(int, input().split())
if H == 0:
    if M-45 >= 0:
        print(H, M-45)
    elif M-45 < 0:
        print(23, (60-45)+M)
else:
    if M-45 >= 0:
        print(H, M-45)
    elif M-45 < 0:
        print(H-1, (60-45)+M)