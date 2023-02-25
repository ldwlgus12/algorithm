def solution(progresses, speeds):
    answer = []
    cnt = 0
    
    while progresses:
        if progresses[0] + speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt:
                answer.append(cnt)
                cnt = 0
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
                
    answer.append(cnt)
    return answer