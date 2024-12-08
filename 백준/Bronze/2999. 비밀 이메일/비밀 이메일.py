message = input()
m = len(message)

a, b = 0, 0

for i in range(1, int(m/2)+1):
    for j in range(i, m+1):
        if i * j == m:
            a, b = i, j

for i in range(a):
    for j in range(b):
        print(message[i+j*a], end='')
        