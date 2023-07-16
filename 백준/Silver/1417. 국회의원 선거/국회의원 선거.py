n = int(input())
a = int(input())
vote = []
result = 0

for _ in range(n - 1):
  vote.append(int(input()))

vote.sort(reverse=True)

if n == 1:
  print(0)
else:
  while vote[0] >= a:
    a += 1
    vote[0] -= 1
    result += 1
    vote.sort(reverse=True)
  print(result)