N = int(input())
num_list = []

for i in range(1, N+1):
    num = int(input())
    num_list.append(num)

sort_list =  sorted(num_list)

for j in range(len(sort_list)):
    print(sort_list[j])