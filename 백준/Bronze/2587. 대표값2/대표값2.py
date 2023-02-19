m = []
for i in range(5):
    n = int(input())
    m.append(n)
x = sum(m)//5
m = sorted(m)
print(x)
print(m[2])