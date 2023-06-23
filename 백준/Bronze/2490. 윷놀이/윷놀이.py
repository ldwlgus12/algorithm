for i in range(3):
    play = list(map(int, input().split()))

    if sum(play) == 3:
        print('A')
    elif sum(play) == 2:
        print('B')
    elif sum(play) == 1:
        print('C')
    elif sum(play) == 0:
        print('D')
    else:
        print('E')

