l = int(input())
n = int(input())

cake = [0] * (l+1)
lst = [0] * (n+1)
most_pieces, audience = 0, 0

for i in range(1, n+1):
    cnt = 0
    p, k = map(int, input().split())
    
    a = k-p
    if most_pieces < a:
        most_pieces = a
        audience = i
        
    for j in range(p, k+1):
        if cake[j] == 0:
            cake[j] = i
            cnt += 1
    lst[i] = cnt
    
print(audience)
print(lst.index(max(lst)))
