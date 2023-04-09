def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0

    for i in routes:
        if i[0] > camera:
            answer += 1
            camera = i[1]

    return answer