alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()
lst = []
name = []

for i in range(len(a)):
	lst.append(alpha[ord(a[i]) - 65])
	lst.append(alpha[ord(b[i]) - 65])

while len(lst) != 2:
	for i in range(1, len(lst)):
		name.append((lst[i] + lst[i-1]) % 10)
	lst = name
	name = []

print(f"{lst[0]}{lst[-1]}")