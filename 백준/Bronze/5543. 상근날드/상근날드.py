nl = []
ml = []

for i in range(3):
    n = int(input())
    nl.append(n)

for j in range(2):
    m = int(input())
    ml.append(m)

print(min(nl) + min(ml) - 50)