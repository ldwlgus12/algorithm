dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    oct_num = input()
    
    if oct_num == '#':
        break
        
    result = 0   
    for i in range(len(oct_num)):
        result += dic[oct_num[i]] * 8**(len(oct_num) - i - 1)
        
    print(result)
    