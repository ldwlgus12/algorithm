import sys
n = int(input())
book = dict()

for i in range(n):
    name = sys.stdin.readline().rstrip()
    
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
        
cnt = 0
sort_book = dict(sorted(book.items()))

for j in sort_book:
    if (sort_book[j]) > cnt:
        cnt = sort_book[j]
        result = j
        
print(result)