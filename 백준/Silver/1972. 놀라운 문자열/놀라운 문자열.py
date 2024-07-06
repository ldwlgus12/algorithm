import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == "*":
        break
    
    for i in range(1, len(string)-1):
        s = set()
        
        for j in range(len(string)-i):
            pair = string[j] + string[j+i]
            
            if pair in s:
                print(string, "is NOT surprising.")
                break
            else:
                s.add(pair)
        else:
            continue
        break
        
    else:
        print(string, "is surprising.")
        