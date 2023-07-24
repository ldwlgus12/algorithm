from math import gcd
import sys

n = int(input())
ring = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    a = gcd(ring[0], ring[i])
    print(f'{ring[0] // a}/{ring[i] // a}')