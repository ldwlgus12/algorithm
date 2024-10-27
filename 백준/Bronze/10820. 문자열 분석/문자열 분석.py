import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break
    
    low, up, num, space = 0, 0, 0, 0

    for i in range(len(s)):        
        if s[i].islower():
            low += 1
            
        elif s[i].isupper():
            up += 1       
            
        elif s[i].isdigit():
            num += 1
            
        else:
            space += 1

    print(low, up, num, space)
    