import sys
input = sys.stdin.readline

s = input().strip()
cnt = 1

for i in range(len(s)-1):
    if  ord(s[i]) >= ord(s[i+1]):
        cnt += 1

print(cnt)
