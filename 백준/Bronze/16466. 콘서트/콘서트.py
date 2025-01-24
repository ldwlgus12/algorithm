n = int(input())
a = sorted(list(map(int, input().split())))
true = True

for i in range(n):
    if (i+1) != a[i]:
        print(i+1)
        true = False
        break
        
if true:
    print(n+1)
    