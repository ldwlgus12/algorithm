import sys
s = set()
cnt = 0

for i in range(int(input())):
    n = sys.stdin.readline().rstrip()
    
    if n == 'ENTER':
        s = set()
    elif n not in s:
        cnt += 1
        s.add(n)
        
print(cnt)