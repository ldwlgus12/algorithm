T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, T+1):
    score_list = []
    N, K = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(N)]

    for a in range(len(score)):
        score[a][0] = 0.35 * score[a][0]
        score[a][1] = 0.45 * score[a][1]
        score[a][2] = 0.2 * score[a][2]
        score_list.append(sum(score[a]))

    stu_score = score_list[K-1]
    score_list.sort(reverse=True)

    div = N//10
    result = score_list.index(stu_score) // div

    print(f'#{i}', grade[result])