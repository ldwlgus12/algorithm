import sys
N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for a in range(N):
    for b in range(M):
        A[a][b] += B[a][b]

for a in A:
    print(*a)