n, q = map(int, input().split())
lst = [int(input()) for _ in range(n)]

for i in range(q):
    t = int(input())
    
    for j in range(n):
        if t < sum(lst[:j+1]):
            print(j+1)
            break
            