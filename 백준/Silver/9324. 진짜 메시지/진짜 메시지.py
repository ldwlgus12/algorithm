def smtp(m):
    alpha = [0] * 26
    check = False
 
    for i in range(len(m)):
        if check:
            check = False
            continue
        alpha[ord(m[i])-65] += 1
 
        if alpha[ord(m[i])-65] == 3:
            if i == len(m) - 1:
                return 'FAKE'
            if m[i] != m[i+1]:
                return 'FAKE'
 
            check = True
            alpha[ord(m[i])-65] = 0
 
    return 'OK'


t = int(input())
for i in range(t):
    m = input()
    print(smtp(m))
    