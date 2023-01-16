numbers = []

for i in range(5):
    num = int(input())
    if num < 40:
        numbers.append(40)
    else:
        numbers.append(num)

print((sum(numbers))//5)