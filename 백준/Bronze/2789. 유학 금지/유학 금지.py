string = list(input())
Donot = 'CAMBRIDGE'

for i in Donot:
    for j in range(len(string)):
        if i == string[j]:
            string[j] = ''
        
for i in string:
    print(i, end='')