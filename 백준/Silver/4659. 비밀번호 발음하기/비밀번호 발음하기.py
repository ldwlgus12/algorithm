vowel = ['a', 'e', 'i', 'o', 'u']
ex = ['ee', 'oo']

while True:
    x, y = 0, 0
    password = input()

    if password == 'end':
        break
    cnt = 0
    
    for i in vowel:
        if i in password:
            cnt +=1 

    if cnt < 1:
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)-2):
        if (password[i] in vowel) and (password[i+1] in vowel) and (password[i+2] in vowel):
            x = 1 
        elif not(password[i] in vowel) and not(password[i+1]in vowel) and not(password[i+2] in vowel):
            x = 1 
            
    if x == 1:
        print(f'<{password}> is not acceptable.')
        continue
        
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                y = 1 
                
    if y == 1:
        print(f'<{password}> is not acceptable.')
        continue
    print(f'<{password}> is acceptable.')
    