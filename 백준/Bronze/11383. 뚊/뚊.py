n, m = map(int, input().split())
str1, str2 = [input() for _ in range(n)], [input() for _ in range(n)]
Eyfa = True 

for i in range(n):
    result = ''
    
    for j in str1[i]:
        result += j*2
    
    if result != str2[i]:
        Eyfa = False
        break

if Eyfa == True:
    print('Eyfa')
else:
    print('Not Eyfa')
