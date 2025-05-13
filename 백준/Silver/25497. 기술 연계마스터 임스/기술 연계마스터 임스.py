n = int(input())
skill = list(str(input()))
cnt = 0
lst = []

for i in skill:
    if (i == 'L' or i == 'S'):
        lst.append(i)

    elif (i == 'K'):
        if 'S' in lst:
            lst.remove('S')
            cnt += 1
        else:
            break

    elif (i == 'R'):
         if 'L' in lst:
            lst.remove('L')
            cnt += 1
         else:
             break

    else:
         cnt += 1

print(cnt)
