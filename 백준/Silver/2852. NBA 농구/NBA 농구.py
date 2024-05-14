import sys
input = sys.stdin.readline

n = int(input())
prev =[0, 0]
t1 = [0, 0]
t2 = [0, 0]

for i in range(n):
    team, time = input().split()
    
    if team == '1':
        t1[0] += 1
    else:
        t2[0] += 1
        
    m, s = map(int, time.split(":"))
    time = m * 60 + s
    
    if t1[0] == t2[0]: 
        if prev[1] == 1:
            t1[1] += time - prev[0]
        else:
            t2[1] += time - prev[0]
        prev[1] = 0
    elif t1[0] > t2[0]: 
        if prev[1] == 0:
            prev[0] = time
            prev[1] = 1
    else: 
        if prev[1] == 0:
            prev[0] = time
            prev[1] = 2

if prev[1] == 1:
    t1[1] += 48*60 - prev[0]
    
if prev[1] == 2:
    t2[1] += 48*60 - prev[0]

print("%02d:%02d" %(t1[1]//60, t1[1]%60))
print("%02d:%02d" %(t2[1]//60, t2[1]%60))
