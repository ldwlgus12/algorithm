a, p = map(int, input().split())
lst = [a]

while True :
  num = 0

  for i in str(lst[-1]) :
    num += int(i) ** p

  if num in lst :
    break

  lst.append(num)

print(lst.index(num))
