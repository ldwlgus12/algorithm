import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}

for i in range(n):
    a, b = sys.stdin.readline().split()
    dict[a] = b

for j in range(m):
    print(dict[sys.stdin.readline().rstrip()])