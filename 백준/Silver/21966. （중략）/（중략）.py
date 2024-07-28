import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

if n <= 25:
    print(s)
    exit()
    
if '.' not in s[11:-12]:
    print(s[:11] + '...' + s[-11:])
    exit()
    
print(s[:9] + '......' + s[-10:])

