import sys
n, m = map(int, sys.stdin.readline().split())
result = 'Yes'

for i in range(2*m):
    books = list(map(int, sys.stdin.readline().split()))
    if books != sorted(books, reverse=True):
        result = 'No'
        break

print(result)
