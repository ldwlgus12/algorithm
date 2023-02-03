for i in range(1, 11):
    T = int(input())
    N = list(map(int, input().split()))
    one = 1

    while True:
        
        N_list = []
        N[0] = N[0] - one
        one += 1
        for a in range(1, len(N)):
            N_list.append(N[a])
        N_list.append(N[0])
        N = N_list

        if N[-1] <= 0:
            N[-1] = 0
            print(f'#{i}',*N)
            break
        else:
            if one == 6:
                one = 1