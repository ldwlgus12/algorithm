while True:
    string = (input())
    if string == 'END':
        break
    else:
        sr = string[::-1]
        print(sr)
