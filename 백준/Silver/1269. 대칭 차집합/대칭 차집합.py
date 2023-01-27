import sys
a, b = map(int, input().split())
A = set(list(map(int, sys.stdin.readline().split())))
B = set(list(map(int, sys.stdin.readline().split())))

A_list = A - B
B_list = B - A

print(len(A_list) + len(B_list))