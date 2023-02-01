import sys
result = 0

N, M = map(int, input().split())
card = list(map(int, sys.stdin.readline().split()))

for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            hap = card[a]+card[b]+card[c]
            if result < hap <= M:
                result = hap

print(result)