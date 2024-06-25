import sys
input = sys.stdin.readline

var = input().replace(',', '').split()

for i in range(1, len(var)):
    var[i] = var[i].replace('[]', '][').replace(';', '')

for i in range(1, len(var)):
    alpha = ''
    result = ''
    
    for j in var[i]:
        if j.isalpha(): 
            alpha += j
        else: 
            result += j
    
    print(var[0] + result[::-1], alpha + ';')
    