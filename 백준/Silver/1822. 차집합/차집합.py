a, b = map(int, input().split())

sa = set(map(int, input().split()))
sb = set(map(int, input().split()))

print(len(sa - sb))
print(*sorted(list(sa - sb)))