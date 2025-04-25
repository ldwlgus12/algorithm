n = int(input())

for _ in range(n):
    v = int(input())
    s = []
    cnt = 0
    result = 0
    
    for i in range(v):
        s.append(int(input()))        
    s.sort(reverse=True)
    
    for i in range(v):
        if s.count(s[i]) >= cnt:
            cnt = s.count(s[i])
            result = s[i]
            
    print(result)
    