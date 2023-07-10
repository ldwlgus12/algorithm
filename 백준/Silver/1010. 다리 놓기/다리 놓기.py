import sys
t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
    else:
        result = 1
        for i in range(m, m-n, -1):
            result *= i
        for j in range(n, 1, -1):
            result = result // j
            
        print(result)