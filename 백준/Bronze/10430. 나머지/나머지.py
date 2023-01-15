num = list(map(int, input().split()))

A = num[0]
B = num[1]
C = num[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)