for _ in range(int(input())):
    n, m = map(int, input().split())
    score = [[0, 0] for _ in range(n)]
    result = []
    
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        score[a-1][0] += p
        score[a-1][1] += q
        score[b-1][0] += q
        score[b-1][1] += p

    for i in range(n):
        if score[i][0] == 0 and score[i][1] == 0:
            result.append(0)
        else:
            result.append(1000 * score[i][0]**2 / (score[i][0]**2 + score[i][1]**2))

    print(int(max(result)))
    print(int(min(result)))
    