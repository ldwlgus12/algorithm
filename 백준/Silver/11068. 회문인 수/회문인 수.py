t = int(input())

for i in range(t):
    num = int(input())
    result = []
    
    for j in range(2, 65):
        lst = []
        a = num
        while a != 0:
            lst.append(a%j)
            a = a//j
            
        for k in range(len(lst)//2):
            if (lst[k] != lst[-1-k]):
                result.append('X')
                break
                
    if len(result) == 63:
        print(0)
    else:
        print(1)
            