n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
result = []

for i in range(n):
    result.append(lst[i]+ 1 + i)

print(max(result) + 1)