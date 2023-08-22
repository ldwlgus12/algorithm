import sys

n = int(sys.stdin.readline())
file = dict()

for i in range(n):
    extend = (sys.stdin.readline().split('.'))[1]
    if not extend in file:
        file[extend] = 1
    else:
        file[extend] += 1

sort_file = sorted(file.items())

for key, value in sort_file:
    print(key.rstrip(), value)