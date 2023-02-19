a,b = map(int, input().split())
n = list(map(int, input().split()))
n = sorted(n, reverse=True)
print(n[b-1])