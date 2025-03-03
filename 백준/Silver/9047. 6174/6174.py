import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = input().rstrip()
    cnt = 0

    while n != "6174":
        cnt += 1
        a = int("".join(sorted(n, reverse=True)))
        b = int("".join(sorted(n)))
        n = str(a-b)

        if len(n) < 4:
            for i in range(4-len(n)):
                n += "0"

    print(cnt)
    