n = int(input())
num = list(map(int, input().split()))
result = []

for i in range(n):
    result.insert(i-num[i], i+1)
    
for i in result:
    print(i, end=' ')