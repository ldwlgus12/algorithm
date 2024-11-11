a, b = map(int, input().split())
lst = [0]

for i in range(46):
    for j in range(i):
        lst.append(i)

print(sum(lst[a:b+1]))
