def prime(a, lst):
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == a:
                    print(i, j, k)
                    return

n = 997
lst = []
arr = [False, False] + ([True] * (n-1))

for i in range(2, n+1):
    if arr[i]:
        lst.append(i)
    for j in range(i*2, n, i):
        arr[j] = False

t = int(input())        
        
for i in range(t):
    a = int(input())
    prime(a, lst)
    