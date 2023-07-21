n, s, e = map(int, input().split())
result = 0

while s != e:
  s -= s//2
  e -= e//2
  result += 1

print(result)