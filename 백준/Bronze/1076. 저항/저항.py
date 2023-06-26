a = input()
b = input()
c = input()

if a == 'black':
    a = '0'
elif a == 'brown':
    a = '1'
elif a == 'red':
    a = '2'
elif a == 'orange':
    a = '3'
elif a == 'yellow':
    a = '4'
elif a == 'green':
    a = '5'
elif a == 'blue':
    a = '6'
elif a == 'violet':
    a = '7'
elif a == 'grey':
    a = '8'
else:
    a = '9'

if b == 'black':
    b = '0'
elif b == 'brown':
    b = '1'
elif b == 'red':
    b = '2'
elif b == 'orange':
    b = '3'
elif b == 'yellow':
    b = '4'
elif b == 'green':
    b = '5'
elif b == 'blue':
    b = '6'
elif b == 'violet':
    b = '7'
elif b == 'grey':
    b = '8'
else:
    b = '9'


if c == 'black':
    c = 1
elif c == 'brown':
    c = 10
elif c == 'red':
    c = 100
elif c == 'orange':
    c = 1000
elif c == 'yellow':
    c = 10000
elif c == 'green':
    c = 100000
elif c == 'blue':
    c = 1000000
elif c == 'violet':
    c = 10000000
elif c == 'grey':
    c = 100000000
else:
    c = 1000000000

string = a+b
result = int(string) * c

print(result)