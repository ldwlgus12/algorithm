n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append(list(map(str, input())))

cnt, sum = 0, 0
result = ''

for j in range(m):
    a, c, g, t = 0, 0, 0, 0
    
    for k in range(n):
        if lst[k][j] == 'A':
            a += 1
        elif lst[k][j] == 'C':
            c += 1
        elif lst[k][j] == 'G':
            g += 1
        elif lst[k][j] == 'T':
            t += 1
            
    if max(a, c, g, t) == a:
        result += 'A'
        sum += c+g+t
    elif max(a,c,g,t) == c:
        result += 'C'
        sum += a+g+t
    elif max(a,c,g,t) == g:
        result += 'G'
        sum += a+c+t
    elif max(a,c,g,t) == t:
        result += 'T'
        sum += a+c+g
    
print(result)
print(sum)
