from itertools import product

n, k = map(int, input().split())
lst = list(map(str, input().split()))
length = len(str(n))

while True:
    arr = list(product(lst, repeat=length))
    result = []

    for i in arr:
        if int("".join(i)) <= n:
            result.append(int("".join(i)))

    if len(result) >= 1:
        print(max(result))
        break
    else: 
        length -=1
        