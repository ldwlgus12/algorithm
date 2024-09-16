n = int(input())

for i in range(n):
    str1, str2 = map(str, input().split())
    sort1 = sorted(str1)
    sort2 = sorted(str2)

    if sort1 == sort2:
        print("Possible")
    else:
        print("Impossible")
        