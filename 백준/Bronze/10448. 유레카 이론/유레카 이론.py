tri = [i * (i+1) // 2 for i in range(1, 46)]
a = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            if i+j+k <= 1000:
                a[i+j+k] = 1

for i in range(int(input())):
    print(a[int(input())])
    