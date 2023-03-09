n = int(input())
l = list(map(int, input().split()))
yl = []
ml = []

for i in range(len(l)):
    yl.append(l[i]//30 + 1)
    ml.append(l[i]//60 + 1)

y = sum(yl) * 10
m = sum(ml) * 15

if y > m:
    print(f'M {m}')
elif y < m:
    print(f'Y {y}')
else:
    print(f'Y M {y}')
