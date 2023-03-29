n = list(input())

if len(n) == 1:
    print('NO')
else:
    left = 1
    for i in range(len(n)-1):
        left *= int(n[i])
        right = 1

        for j in range(i+1, len(n)):
            right *= int(n[j])
        
        if left == right:
            break
            
    if left == right:
        print('YES')
    else:
        print('NO')