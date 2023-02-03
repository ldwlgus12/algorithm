T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(N)]
    num_list = []

    for a in range(N-M+1):
        for b in range(N-M+1):
            fly = 0

            for c in range(M):
                for d in range(M):
                    fly += num[a+c][b+d]
            num_list.append(fly)

    print(f'#{i}',max(num_list))