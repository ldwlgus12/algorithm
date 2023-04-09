def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    link = set([costs[0][0]])  
    while len(link) != n:   
        for i in costs:
            if i[0] in link and i[1] in link: 
                continue
            if i[0] in link or i[1] in link:   
                link.update([i[0], i[1]])   
                answer += i[2]
                break
                
    return answer