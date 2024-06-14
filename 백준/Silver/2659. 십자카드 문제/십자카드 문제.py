import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
cnt = 1

def clock(n):
    min_num = int(''.join(map(str, n)))
    
    for i in range(1, 4):
        a = int(''.join(map(str, n[i:] + n[:i])))
        
        if min_num > a:
            min_num = a
            
    return min_num

clock_num = clock(num)

for i in range(1111, clock_num):
    if '0' not in list(str(i)) and i == clock(list(map(int, str(i)))):
        cnt += 1
        
print(cnt)
