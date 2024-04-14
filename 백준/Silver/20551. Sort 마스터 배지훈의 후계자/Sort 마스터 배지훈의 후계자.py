import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)])
dic = dict()

for i in range(n):
    if lst[i] not in dic:
    	dic[lst[i]] = i

for i in range(m):
    d = int(input())
    
    if d in dic:
        print(dic[d])
    else:
        print(-1)
    