N = int(input())
six = 666
result = 0

while True:
    if '666' in str(six):
        result += 1
    if result == N:
        print(six)
        break
    six += 1