num_list = []

for i in range(7):
    num = int(input())
    if num % 2 != 0:
        num_list.append(num)

if len(num_list) == 0:
    print('-1')
else:
    print(sum(num_list))
    print(min(num_list))