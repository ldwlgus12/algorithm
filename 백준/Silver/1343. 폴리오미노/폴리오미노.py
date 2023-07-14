a = input()

a = a.replace("XXXX", "AAAA")
a = a.replace("XX", "BB")

if 'X' in a:
    print(-1)
    
else:
    print(a)