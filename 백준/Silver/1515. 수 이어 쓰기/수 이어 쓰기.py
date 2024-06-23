n = input()
result = 0

while True:
    result += 1
    num = str(result)
    
    while len(num) > 0 and len(n) > 0:
        if num[0] == n[0]:
            n = n[1:]            
        num = num[1:]
        
    if n == '':
        print(result)
        break
        