t = int(input())

for i in range(t):
    n = int(input())
    closet = {}
    
    for j in range(n):
        cloth = list(input().split())
        
        if cloth[1] in closet:
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
            
    result = 1
    
    for a in closet:
        result *= (len(closet[a])+1)
        
    print(result - 1)
    