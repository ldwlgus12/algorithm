n = int(input())
m = list(map(int, input().split()))
m = sorted(m)
x = 0
y = 0
for i in range(len(m)):
    x += m[i]
    y += x
print(y)