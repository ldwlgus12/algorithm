a,b = map(int, input().split())
c = list(map(int, input().split()))
d = a*b

for i in range(len(c)):
    if d == c[i]:
        print(0)
    else:
        print((d-c[i])*-1, end=' ')