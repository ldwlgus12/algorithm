n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(len(b)) :
  for j in range(len(a)) :
    if b[i] > a[j] :
      continue
    
    a[j] -= b[i]
    break

print(sum(a))
