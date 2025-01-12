for i in range(int(input())):
    input()	
    
    n, m = map(int, input().split())    
    sj = sorted(list(map(int, input().split())), reverse=True)
    sb = sorted(list(map(int, input().split())), reverse=True)
    
    while sj and sb:
        if sj[-1] >= sb[-1]:
            sb.pop()
        else:
            sj.pop()
    
    if sj:
        print('S')
    elif sb:
        print('B')
    else:
        print('C')
        