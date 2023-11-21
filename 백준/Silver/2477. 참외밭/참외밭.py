k = int(input())
x = [] 
y = [] 
d_d = [] 
b_d = []

for i in range(6):
    direc, dist = map(int, input().split())
    d_d.append([direc, dist])
    
    if d_d[i][0] == 1 or d_d[i][0] == 2:
        x.append(d_d[i][1])
    
    if d_d[i][0] == 3 or d_d[i][0] == 4:
        y.append(d_d[i][1])

for j in range(6):
    if d_d[j][0] == d_d[(j+2)%6][0]:
        b_d.append(d_d[(j+1)%6][1])
        
print(((max(x)*max(y)) - (b_d[0]*b_d[1])) * k)
