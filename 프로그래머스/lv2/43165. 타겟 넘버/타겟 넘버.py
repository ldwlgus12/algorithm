def solution(numbers, target):
    result = [0]          # 모든 계산 결과 담는 곳     
    cnt = 0 

    for num in numbers : 
        temp = []

        # 자손 노드 
        for i in result : 
            temp.append(i + num)    # 더하는 경우 
            temp.append(i - num)    # 빼는 경우 

        result = temp 

    # 모든 경우의 수 계산 후 target과 같은지 확인 
    for j in result : 
        if j == target : 
            cnt += 1


    return cnt