import sys
n = int(sys.stdin.readline())
name = {'ChongChong'}

for i in range(1, n+1):
    a, b = sys.stdin.readline().rstrip().split()

    if a in name:
        name.add(b)

    if b in name:
        name.add(a)

print(len(name))
