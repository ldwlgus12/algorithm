n, l, d = map(int, input().split())
l += 5
num = 0
sec = d

for i in range(n):
    num += l
    while True:
        if sec < num-5: 
            sec += d
        else: 
            break
            
    if num-5 <= sec < num: 
        break
        
print(sec)
