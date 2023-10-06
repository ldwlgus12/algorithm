n = int(input())
tip = []

for i in range(n) :
  tip.append(int(input()))

tip.sort(reverse=True)
result = 0

for j in range(n) :
  a = tip[j] - j

  if a > 0 :
    result += a

print(result)