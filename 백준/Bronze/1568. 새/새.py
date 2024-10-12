n = int(input())
cnt = 1
time = 0

while n >= 1:
    if n < cnt:
        cnt = 1
    
    n = n - cnt
    cnt += 1
    time += 1

print(time)
