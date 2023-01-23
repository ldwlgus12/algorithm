import sys

T = int(input())

for i in range(1, T+1):
    num = list(map(int, sys.stdin.readline().split()))
    print(sum(num))