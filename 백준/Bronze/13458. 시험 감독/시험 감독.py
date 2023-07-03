n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
result = n

for i in a:
    i -= b
    if i > 0:
        if i % c:
            result += (i // c) + 1
        else:
            result += (i // c)
        
print(result)