n = [False, False] + [True] * 4000000

for i in range(2, 4000000):
    if n[i]:
        for j in range(i+i, 4000000, i):
            n[j] = False

a, b, d = map(int, input().split())
result = 0

for i in range(a, b+1):
    if n[i]:
        if str(d) in str(i):
            result += 1
            
print(result)
