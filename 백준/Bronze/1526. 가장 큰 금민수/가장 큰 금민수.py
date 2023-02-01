N = int(input())

while True:
    true = True
    for i in str(N):
        if i != '4' and i != '7':
            true = False
            N -= 1
        
    if true:
        print(N)
        break