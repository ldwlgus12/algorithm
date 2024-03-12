n = int(input())
lst = []

for i in range(n):
    s, e = map(int, input().split(" "))
    lst.append((s, e))

lst.sort(key=lambda x: (x[1], x[0]))
time = 0
result = 0

for i in lst:
    if time <= i[0]:
        time = i[1]
        result += 1

print(result)