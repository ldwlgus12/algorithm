import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
cnt = 0

for i in range(n):
    p, l = map(int, input().split())
    mile = list(map(int, input().split()))
    mile.sort(reverse = True)

    if p < l:
        lst.append(1)
    else:
        lst.append(mile[l-1])

lst.sort()

for i in lst:
    if m - i >= 0:
        m -= i
        cnt += 1
    else:
        break

print(cnt)
