import math
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

bj = a1 * b2 + a2 * b1
bm = b1 * b2
c = math.gcd(bj, bm)

bj //= c
bm //= c

print(bj, bm)