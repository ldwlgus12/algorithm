num = int(input())
result = 0
result_list = []

numbers = list(map(int, input().split()))

for i in range(num):
    if numbers[i] == 1:
        result += 1
        result_list.append(result)
    else:
        result = 0
        result_list.append(result)

print(sum(result_list))