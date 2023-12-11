import sys
n, m = map(int, sys.stdin.readline().split())

def cnt_2(n):
    if n < 2:
        return 0
    cnt = 0
    
    while n >= 2:
        cnt += n//2
        n = n//2
    return cnt

def cnt_5(n):
    if n < 5:
        return 0
    cnt = 0
    
    while n >= 5:
        cnt += n//5
        n //= 5
    return cnt

cnt_two = cnt_2(n) - cnt_2(n-m) - cnt_2(m)
count_five = cnt_5(n) - cnt_5(n-m) - cnt_5(m)

print(min(cnt_two, count_five))