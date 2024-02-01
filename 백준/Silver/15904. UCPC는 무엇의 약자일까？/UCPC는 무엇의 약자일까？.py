string = input()
alpha = ['U', 'C', 'P', 'C']
cnt = 0

for i in alpha:
    if i in string:
        cnt += 1
        string = string[string.index(i) + 1:]
    else:
        print('I hate UCPC')
        break
        
if cnt == 4:
    print('I love UCPC')