def solution(clothes):
    cloth = {}
    answer = 1
    
    for a in clothes:
        if a[1] in cloth.keys():
            cloth[a[1]].append(a[0])
        else:
            cloth[a[1]] = [a[0]]
    
    for value in cloth.values():
        answer *= len(value) + 1
    
    return answer - 1