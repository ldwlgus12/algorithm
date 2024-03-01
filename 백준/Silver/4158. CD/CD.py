import sys

while True:
    n, m = map(int,sys.stdin.readline().split())
    dic = {}
    cnt = 0
    
    if n == 0 and m == 0:
        break
    
    for i in range(n):
        cd = int(sys.stdin.readline())
        dic[cd] = 1

    for i in range(m):
        cd = int(sys.stdin.readline())
        if cd in dic:
            cnt += 1

    print(cnt)