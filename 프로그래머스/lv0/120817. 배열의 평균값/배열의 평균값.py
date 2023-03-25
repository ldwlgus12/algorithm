def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)):
        answer += numbers[i]
    
    return answer / len(numbers)