s = int(input())
cnt = 0
result = 0

while True:
    cnt += 1
    result += cnt
    if result > s:
        break

print(cnt-1)