i = 1
while True:
    n = list(map(int, input().split()))
    if 0 in n:
        break
    else:
        print(f'Case {i}: Sorting... done!')
        i += 1