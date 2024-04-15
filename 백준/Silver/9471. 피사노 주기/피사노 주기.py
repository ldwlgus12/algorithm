import sys
input = sys.stdin.readline

def cycle(num):
    mod1, mod2 = 1, 2
    cnt = 1
    
    while True:
        if mod1 % num == 1 and mod2 % num == 1:
            break

        cnt += 1
        mod1, mod2 = mod2, (mod1 + mod2) % num
    return cnt

p = int(input())
    
for i in range(p):
    n, m = map(int, input().split())
    cnt = cycle(m)
    print(f"{n} {cnt}")
        