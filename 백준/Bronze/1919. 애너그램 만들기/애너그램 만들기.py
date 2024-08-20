a = list(input())
b = list(input())
cnt = 0

while cnt < len(a):
    if a[cnt] in b:
        b.remove(a[cnt])
        a.remove(a[cnt])
        cnt -= 1
    cnt += 1
    
print(len(a)+len(b))
