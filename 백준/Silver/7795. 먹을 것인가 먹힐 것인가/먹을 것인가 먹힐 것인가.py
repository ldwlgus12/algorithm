t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 
    a.sort()
    b.sort()
 
    cnt = 0
    result = 0
 
    for j in range(n):
        while True:
            if cnt == m or a[j] <= b[cnt]:
                result += cnt
                break
            else:
                cnt += 1
 
    print(result)
    