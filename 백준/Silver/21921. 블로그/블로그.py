import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

if max(visit) == 0:
    print("SAD")
else:
    value = sum(visit[:x])
    max_value = value
    cnt = 1
    
    for i in range(x, n):
        value += visit[i]
        value -= visit[i-x]
        
        if value > max_value:
            max_value = value
            cnt = 1
            
        elif value == max_value:
            cnt += 1
            
    print(max_value)
    print(cnt)
    