n, l, k = map(int,input().split())
result = []

for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        result.append(140)
    elif sub1 <= l:
        result.append(100)
        
result = sorted(result, reverse=True)
print(sum(result[:k]))
