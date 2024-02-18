n = int(input())
lst = []

for i in range(n):
    name = input()
    lst.append(name)

if sorted(lst) == lst:
    print("INCREASING")
elif sorted(lst, reverse=True) == lst:
    print("DECREASING")
else:
    print("NEITHER")
        