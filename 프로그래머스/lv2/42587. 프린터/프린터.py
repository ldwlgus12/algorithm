def solution(priorities, location):
    answer = 0

    while True:
        max_n = max(priorities)
        for i in range(len(priorities)):
            if max_n == priorities[i]:
                answer += 1
                priorities[i] = 0
                max_n = max(priorities)
                if i == location:
                    return answer