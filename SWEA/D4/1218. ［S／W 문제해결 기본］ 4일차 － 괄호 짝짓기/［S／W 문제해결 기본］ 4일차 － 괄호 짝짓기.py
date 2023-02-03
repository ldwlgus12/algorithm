
for i in range(1,11):
    T = int(input())
    string = list(input())

    a = 0
    b = 0
    c = 0
    d = 0

    for j in range(len(string)):
        if string[j] == '(':
            a += 1
        elif string[j] == ')':
            a -= 1

        elif string[j] == '[':
            b += 1
        elif string[j] == ']':
            b -= 1


        elif string[j] == '{':
            c += 1
        elif string[j] == '}':
            c -= 1


        elif string[j] == '<':
            d += 1
        elif string[j] == '>':
            d -= 1

    if a == 0 and b == 0 and c == 0 and d == 0:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
