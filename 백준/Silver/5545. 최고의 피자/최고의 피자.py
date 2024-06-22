n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []                         

for i in range(n) :
    d.append(int(input()))

d.sort(reverse = True) 
result = c/a        

for i in range(1, len(d)+1) :
    cal = c + sum(d[:i])
    cost = a + b * len(d[:i])
    
    if cal/cost > result :
        result = cal/cost
    else :
        break

print(int(result))
