import sys
input = sys.stdin.readline

n, i = map(int, input().split())
handle = sorted([input().rstrip() for _ in range(n)])

print(handle[i-1])
