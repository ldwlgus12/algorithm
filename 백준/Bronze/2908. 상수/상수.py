a, b = input().split()
ar = a[::-1]
br = b[::-1]

if int(ar) > int(br):
    print(ar)
else:
    print(br)