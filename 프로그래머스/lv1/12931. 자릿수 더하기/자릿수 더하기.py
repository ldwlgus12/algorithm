def solution(n):
    nl = str(n)
    answer = 0
    li = list(nl)
    
    for i in range(len(li)):
        answer += int(li[i])

    return answer