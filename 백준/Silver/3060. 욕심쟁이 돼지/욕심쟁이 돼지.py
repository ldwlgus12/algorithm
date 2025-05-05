for _ in range(int(input())):
    n = int(input())
    food = sum(list(map(int, input().split())))
    day = 1
    
    while n >= food:
        day += 1
        food *= 4
        
    print(day)
    