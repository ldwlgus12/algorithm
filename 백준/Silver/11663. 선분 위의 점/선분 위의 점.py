import sys
input = sys.stdin.readline

def line(v, d):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right)//2

        if v < c[mid]:
            right = mid-1
        elif v > c[mid]:
            left = mid+1
        else:
            return mid

    if d == 0:
        return left
    else:
        return right


n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))

for i in range(m):
    s, e = map(int, input().split())
    l, r = line(s, 0), line(e, 1)
    print(r-l+1)
    