n = int(input())

for i in range(n) :
    p = int(input())
    ex_price = 0
    ex_name = ''
    
    for j in range(p) :
        c, name = input().split()
        
        if int(c) > ex_price :
            ex_price = int(c)
            ex_name = name
  
    print(ex_name)
    