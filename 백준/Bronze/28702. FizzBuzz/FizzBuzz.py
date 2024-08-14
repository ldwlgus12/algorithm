for i in range(3, 0, -1):
    n = input()
    if n not in ['FizzBuzz', 'Fizz', 'Buzz']:
        m = int(n) + i

if m % 15 == 0:
    print('FizzBuzz')
elif m % 3 == 0:
    print('Fizz')
elif m % 5 == 0:
    print('Buzz')
else:
    print(m)
    