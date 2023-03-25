import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

print(m[0] * m[-1])