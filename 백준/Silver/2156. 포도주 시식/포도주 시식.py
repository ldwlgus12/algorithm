n = int(input())
wine = []
arr = [0]*n

for i in range(n):
    wine.append(int(input()))

arr[0] = wine[0]

if n > 1:
    arr[1] = wine[0] + wine[1]

if n > 2:
    arr[2] = max(wine[2]+wine[1], wine[2]+wine[0], arr[1])

for i in range(3, n):
    arr[i] = max(arr[i-1], arr[i-3]+wine[i-1]+wine[i], arr[i-2]+wine[i])

print(arr[n-1])
