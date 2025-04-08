n = int(input())

for _ in range(n):
    x = list(input())
    
    for i in range(len(x)-1, 0, -1):
        if int(x[i]) >= 5:
            x[i-1] = str(int(x[i-1])+1)
        x[i] = '0'

    for j in range(len(x)):
        print(x[j], end='')
    print()
    