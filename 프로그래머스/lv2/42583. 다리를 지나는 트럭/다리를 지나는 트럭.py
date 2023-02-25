def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = [0 for _ in range(bridge_length)]
    
    while b:
        answer += 1
        b.pop(0)
        
        if truck_weights:
            if sum(b) + truck_weights[0] <= weight:
                b.append(truck_weights.pop(0))
            else:
                b.append(0)
                
    return answer