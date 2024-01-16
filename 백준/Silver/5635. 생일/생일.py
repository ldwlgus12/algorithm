import sys
lst = []

for i in range(int(sys.stdin.readline())):
    n, d, m, y = sys.stdin.readline().rstrip().split()
    d, m, y = map(int, (d, m, y))
    lst.append((y, m, d, n))
    
lst.sort()

print(lst[-1][3])
print(lst[0][3])