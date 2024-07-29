import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    poke = input().rstrip()
    dic[i] = poke
    dic[poke] = i

for i in range(m):
    p = input().rstrip()
    
    if p.isdigit():
        print(dic[int(p)])
    else:
        print(dic[p])
        