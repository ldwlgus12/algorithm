import sys
input = sys.stdin.readline

while True:
    text = []
    n = int(input())
    
    if n == 0:
        break
    for i in range(n):
        a = input().strip().split(" ")
        text.append(a)
        
    cnt = 1
    for i in range(n):
        for j in range(len(text[i])):
            if cnt <= sum(map(len, text[i][:j+1])) + j + 1:
                cnt = sum(map(len, text[i][:j+1])) + j + 1
                break
                
    print(cnt)
    