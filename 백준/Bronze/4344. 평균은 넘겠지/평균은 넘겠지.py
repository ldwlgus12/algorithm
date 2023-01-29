import sys
C = int(input())

for i in range(C):
    ave = 0
    student = 0
    percent = 0
    score = list(map(int, sys.stdin.readline().split()))
    score_middle = score[1:]
    ave = (sum(score_middle)/score[0])

    for j in range(len(score_middle)):
        if score_middle[j] > ave:
            student += 1
    
    percent = (100*(student/score[0]))
    print(f'{percent:.3f}%')