import sys
input = sys.stdin.readline

t = int(input())
lst = []
result = []
cnt = 0

for i in range(t):
    n = int(input())
    data1 = input()
    data2 = input()

    for j in range(n):
        if data1[j] != data2[j]:
            lst.append(data1[j])
            
    if lst.count('B') >= lst.count('W'):
        cnt = lst.count('B')
    else:
        cnt = lst.count('W')
        
    result.append(cnt)
    lst = []
    
for i in result:
    print(i)
