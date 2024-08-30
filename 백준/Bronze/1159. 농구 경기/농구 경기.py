n = int(input())
lst = []
result = []

for i in range(n):
    first = input()
    lst.append(first[0])

set_lst = set(lst)

for i in set_lst:
    if lst.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")
    