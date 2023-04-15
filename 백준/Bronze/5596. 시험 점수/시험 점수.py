a = list(map(int, input().split()))
b = list(map(int, input().split()))

mk = sum(a)
ms = sum(b)

if mk > ms:
    print(mk)
elif mk < ms:
    print(ms)
else:
    print(mk)