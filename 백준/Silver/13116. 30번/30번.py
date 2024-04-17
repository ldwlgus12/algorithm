import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    while True:
        if a == b:
            print(a*10) 
            break
        elif a > b:
            a //= 2
        else:
            b //= 2
            