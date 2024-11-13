n = int(input())
s = input()

c = s.count('LL')

if c <= 1:
    print(n)
else:
    print(n + 1 - c)
    