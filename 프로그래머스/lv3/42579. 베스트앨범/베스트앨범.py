def solution(genres, plays):
    answer = []
    gen = []
    total = {}
    
    gen = [[genres[i], plays[i], i] for i in range(len(genres))]
    gen = sorted(gen, key=lambda x: (x[0], -x[1], x[2])) 
    
    for i in range(len(genres)):    
        if genres[i] in total.keys():   
            total[genres[i]] += plays[i]   
        else:                               
            total[genres[i]] = plays[i] 

    total = sorted(total.items(), key=lambda x: -x[1])
    
    for a in total: 
        count = 0
        for b in gen:   
            if a[0] == b[0]:    
                count += 1      
                if count > 2:   
                    break       
                else:           
                    answer.append(b[2])
    return answer