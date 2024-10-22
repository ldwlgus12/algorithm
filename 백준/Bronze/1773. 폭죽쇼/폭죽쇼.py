import sys
input = sys.stdin.readline

n, c = map(int, input().split())
fw = [0] * (c+1)

for i in range(n):
    t = int(input())
    
    if t == 1:
        print(c)
        exit()
    else:
        for j in range(t, c+1, t):
            fw[j] = 1

print(sum(fw))
