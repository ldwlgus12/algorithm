n = int(input())
dic = {}
cnt = 0
 
for i in range(n):
    a, b = map(int, input().split())
    
    if a not in dic:
        dic[a] = b
    else:
        if dic[a] != b:
            cnt += 1
            dic[a] = b

print(cnt)
