condo = []

for i in range(int(input())):
    d, c = map(int, input().split())
    condo.append([d, c])
    
condo.sort()
cost = 10001
cnt = 0

for i in condo:
    a = i[1]
    if a < cost:
        cost = a
        cnt += 1
        
print(cnt)
