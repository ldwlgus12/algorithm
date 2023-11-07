import itertools

while True:
    lst = list(map(int, input().split()))

    k = lst[0]
    s = lst[1:]

    for i in itertools.combinations(s, 6):
        print(*i)

    if k == 0:
        exit()
        
    print()