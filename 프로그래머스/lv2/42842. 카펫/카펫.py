def solution(brown, yellow):
    answer = []

    y_x = 0
    y_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_x = int(yellow/i)
            y_y = i
            if y_x * 2 + y_y * 2 + 4 == brown:
                answer.append(y_x+2)
                answer.append(y_y+2)

                return sorted(answer, reverse=True)
            
    return answer