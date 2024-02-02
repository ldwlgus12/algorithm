import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))
    
for i in sorted(lst):
    print(i)
