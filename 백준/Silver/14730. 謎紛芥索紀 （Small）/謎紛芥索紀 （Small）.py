n = int(input())
result = 0

for i in range(n):
    c, k = map(int, input().split())
    result += c * k
    
print(result)