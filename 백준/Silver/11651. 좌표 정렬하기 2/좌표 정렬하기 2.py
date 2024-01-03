lst = []

for i in range(int(input())):
	x, y = map(int, input().split())
	lst.append((x, y))

lst.sort(key = lambda x: (x[1], x[0]))

for j in lst:
	print(j[0], j[1])