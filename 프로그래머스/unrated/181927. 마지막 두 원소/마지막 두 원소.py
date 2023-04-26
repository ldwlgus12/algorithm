def solution(num_list):
    num_list.reverse()

    if num_list[0] > num_list[1]:
        num = num_list[0] - num_list[1]    
        num_list.reverse()
        num_list.append(num)
    else:
        num = num_list[0] * 2
        num_list.reverse()
        num_list.append(num)
    return num_list