import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))

result = []
high = 0
cnt = 0

for i in height:
    if i > high:
        high = i
        cnt = 0
    else:
        cnt += 1
        
    result.append(cnt)
    
print(max(result))
