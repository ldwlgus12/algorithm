x = input()
cnt = 0 

while len(x) > 1: 
    cnt += 1 
    result = 0
    
    for i in x:
        result += int(i) 
    x = str(result) 

print(cnt) 

if int(x)%3 == 0: 
    print("YES")
else:
    print("NO")