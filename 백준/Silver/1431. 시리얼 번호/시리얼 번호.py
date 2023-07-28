import sys
input = sys.stdin.readline
a = []

for _ in range(int(input())):
    s = input().rstrip()
    sum = 0
    
    for i in s:
        if i.isdigit():
            sum += int(i)
    a.append((s, sum))
    
a.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in a:
    print(i[0])