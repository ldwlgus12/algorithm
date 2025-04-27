r, c = map(int, input().split())
parking = [input().strip() for _ in range(r)]
lst = [0] * 5

for i in range(r-1):
    for j in range(c-1):
        block = [parking[i][j], parking[i][j+1],
            parking[i+1][j], parking[i+1][j+1]]

        if '#' in block:
            continue

        broken = block.count('X')
        lst[broken] += 1

for i in lst:
    print(i)
