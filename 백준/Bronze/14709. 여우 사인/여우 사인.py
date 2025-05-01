n = int(input())
fingers = set()

for _ in range(n):
    a, b = map(int, input().split())
    fingers.add(frozenset([a, b]))

fox_sign = {
    frozenset([1, 3]),
    frozenset([1, 4]),
    frozenset([3, 4])
}

if fingers == fox_sign:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")
    