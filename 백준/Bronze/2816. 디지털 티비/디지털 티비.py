n = int(input())
ch = list(input() for _ in range(n))
lst = []
cnt = 0

while ch[cnt] != 'KBS1':
    cnt += 1
    lst.append(1)
    
for i in range(cnt):
    lst.append(4)
    
cnt = 0
ch.remove('KBS1')
ch = ['KBS1'] + ch

while ch[cnt] != 'KBS2':
    cnt += 1
    lst.append(1)
    
for i in range(cnt-1):
    lst.append(4)
    
print(''.join(map(str, lst)))
