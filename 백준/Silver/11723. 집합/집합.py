import sys
n = int(sys.stdin.readline())
s = set()

for i in range(n):
    a = sys.stdin.readline().split()

    if len(a) == 1:
        a0 = a[0]
    else:
        a0, a1 = a

    if a0 == 'add':
        s.add(int(a1))
    elif a0 == 'remove':
        if int(a1) in s:
            s.remove(int(a1))
    elif a0 == 'check':
        if int(a1) in s:
            print(1)
        else:
            print(0)
    elif a0 == 'toggle':
        if int(a1) in s:
            s.remove(int(a1))
        else:
            s.add(int(a1))
    elif a0 == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s.clear()