while True:
    n = int(input())
    if n == 0:
        break

    max_height = 0
    lst = []
    for i in range(n):
        name, height = input().split()
        height = float(height)
        
        if height > max_height:
            lst = [name]
            max_height = height
        elif height == max_height:
            lst.append(name)
            
    print(*lst)
        