n = int(input())
s, e = 1, 1
cnt, result = 0, 1

while e != n:
    if result < n:
        e += 1
        result += e
    elif result > n:
        result -= s
        s += 1
    else:
        cnt += 1
        e += 1
        result += e
        
print(cnt + 1)