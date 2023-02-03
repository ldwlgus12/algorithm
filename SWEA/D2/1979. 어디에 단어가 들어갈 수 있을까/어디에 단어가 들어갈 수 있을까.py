T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    hap_list = []
    result = 0
    result1 = 0

    for a in range(len(puzzle)):
        hap = 0
        for b in range(len(puzzle)):
            if puzzle[a][b] == 0:
                if hap == K:
                    result += 1
                hap = 0
            else:
                hap += 1
        if hap == K:
            result += 1

    for b in range(len(puzzle)):
        hap = 0
        for a in range(len(puzzle)):
            if puzzle[a][b] == 0:
                if hap == K:
                    result += 1
                hap = 0
            else:
                hap += 1
        if hap == K:
            result += 1   

    print(f'#{i} {result}')
    