t = int(input())

for i in range(t):
    n = int(input())
    key1 = list(map(str, input().split()))
    key2 = list(map(str, input().split()))
    pw = list(map(str, input().split()))
    
    lst = []
    result = ''
    
    for j in range(n):
        lst.append(key2.index(key1[j]))
        
    for k in range(n):
        result += (pw[lst[k]] + ' ')
        
    print(result)