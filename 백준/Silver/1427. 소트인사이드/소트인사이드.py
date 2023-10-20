lst = list(map(int, str(input())))
lst.sort(reverse=True)

for i in lst:
    print(i, end='')