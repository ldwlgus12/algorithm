m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    a = int(i ** 0.5) ** 2
    if i == a:
        lst.append(i)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
    