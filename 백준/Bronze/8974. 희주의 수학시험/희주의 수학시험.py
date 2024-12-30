a, b = map(int, input().split())
lst = []

for i in range(1, b+1):
    if len(lst) < b:
        for j in range(i):
            lst.append(i)
    
print(sum(lst[a-1:b]))
