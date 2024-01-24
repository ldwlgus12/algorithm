a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
cnt = 0
result = ''

for i in range(m):
    cnt += lst[m-i-1] * a ** i

while cnt:
    result = ' ' + result
    result = str(cnt%b) + result
    cnt //= b

print(result)
