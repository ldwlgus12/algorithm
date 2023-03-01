import sys
n = int(input())
nl = set(map(int, sys.stdin.readline().split()))
m = int(input())
ml = list(map(int, sys.stdin.readline().split()))

for i in ml:
    print(1) if i in nl else print(0) 