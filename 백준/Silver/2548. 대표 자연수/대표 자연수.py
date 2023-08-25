n = int(input())
nl = list(map(int, input().split()))
nl.sort()

if n % 2 == 0:
    print(nl[n//2 - 1])
else:
    print(nl[n//2])