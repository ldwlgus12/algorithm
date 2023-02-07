N = int(input())
body = []
for i in range(N):
    x, y = map(int, input().split())
    body.append((x,y))

for a in body:
    result = 1
    for b in body:
        if a[0] < b[0] and a[1] < b[1]:
            result += 1

    print(result, end=" ")