n = int(input())
check = [False] + [True] * 103
lst = []
num = []

for i in range(2, 104):
    if check[i]:
        lst.append(i)
        for j in range(2*i, 104, i):
            check[j] = False

for i in range(1, len(lst)):
    num.append(lst[i] * lst[i-1])

for i in num:
    if i > n:
        print(i)
        break