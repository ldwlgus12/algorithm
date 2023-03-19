def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]

    cnt = [0,0,0]
    right = []

    for i in range(len(answers)):
        if answers[i] == one[(i%5)]:
            cnt[0] += 1
        if answers[i] == two[(i%8)]:
            cnt[1] += 1
        if answers[i] == thr[(i%10)]:
            cnt[2] += 1    

    for j in range(3):
        if cnt[j] == max(cnt):
            right.append(j+1)
            
    return right