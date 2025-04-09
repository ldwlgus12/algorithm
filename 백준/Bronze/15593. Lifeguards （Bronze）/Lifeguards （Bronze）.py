n = int(input())
lifeguards = [0]*1000
work = []
result = 0

for _ in range(n):
    s, e = map(int, input().split())
    work.append((s, e))
    for i in range(s, e):
        lifeguards[i] += 1

for i in work:
    s, e = i[0], i[1]
    for j in range(s, e):
        lifeguards[j] -= 1
        
    time = 0    
    for j in lifeguards:
        if j > 0:        
            time += 1
            
    result = max(time, result) 
    for j in range(s, e):
        lifeguards[j] += 1  
        
print(result)
