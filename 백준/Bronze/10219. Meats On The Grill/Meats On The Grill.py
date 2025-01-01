for i in range(int(input())):
    h, w = map(int, input().split())
    
    for j in range(h):
        grill = input()
        a = w-1
        
        while a >= 0:
            print(grill[a], end='')
            a = a-1
        print()
