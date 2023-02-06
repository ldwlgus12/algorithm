string = input()
happy = string.count(':-)')
sad = string.count(':-(')
    
if ':-)' in string or ':-(' in string:
    if happy == sad:
        print('unsure')
    elif happy > sad:
        print('happy')
    elif happy < sad:
        print('sad')
else:
    print('none')