t = int(input())

for _ in range(t):
    s, p = map(str, input().split())
    cnt = s.count(p)
    
    result = s.replace(p, "")
    print(cnt + len(result))
    