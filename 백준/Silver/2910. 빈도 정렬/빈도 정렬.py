import sys
n, c = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
dict = {}

for i in lst:
    if i not in dict:
        dict[i] = 0

    dict[i] += 1

dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for key, value in dict:
    for j in range(value):
        print(str(key), end=" ")
        