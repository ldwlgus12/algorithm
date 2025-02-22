n = int(input())
topping = list(input().split())
lst = set()

for i in topping:
    if i.endswith("Cheese"):
        lst.add(i)

if len(lst) >= 4:
    print("yummy")
else:
    print("sad")
    