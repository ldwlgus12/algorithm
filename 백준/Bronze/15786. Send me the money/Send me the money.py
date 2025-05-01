import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input().rstrip()

for _ in range(m):
    postit = input().rstrip()
    cnt = 0

    for i in postit:
        target = s[cnt]

        if i != target:
            continue        
        cnt += 1
        
        if n <= cnt:
            break
    
    if n == cnt:
        print('true')
    else:
        print('false')
    