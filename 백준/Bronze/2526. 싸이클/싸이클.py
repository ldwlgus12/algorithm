n, p = map(int, input().split())

lst = []
a = n

while True:
    a = (a*n) % p
    if a in lst:
        print(len(lst) - lst.index(a))
        break
        
    lst.append(a)
    