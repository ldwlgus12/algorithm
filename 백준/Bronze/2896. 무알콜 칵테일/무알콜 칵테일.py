a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

m = min(a/i, b/j, c/k)
print(a-i*m, b-j*m, c-k*m)
