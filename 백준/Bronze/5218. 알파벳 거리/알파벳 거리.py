t = int(input())

for i in range(t):
    a, b = input().split()
    lst = []
    
    for j in range(len(a)):
        if ord(a[j]) > ord(b[j]):
            lst.append(26 - (ord(a[j]) - ord(b[j])))
        else:
            lst.append(ord(b[j]) - ord(a[j]))
            
    print("Distances:", *lst)
    