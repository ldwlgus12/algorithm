def solution(money):
    house1 = [0] * len(money)
    house2 = [0] * len(money)
    
    # 1번 집을 터는 경우
    house1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집은 털지 못함
        house1[i] = max(house1[i - 1], house1[i - 2] + money[i])
    
    # 1번 집을 안터는 경우
    house1[0] = 0
    for i in range(1, len(money)):
        house2[i] = max(house2[i - 1], house2[i - 2] + money[i])

    return max(house1[-2], house2[-1])