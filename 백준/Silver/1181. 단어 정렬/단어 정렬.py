N = int(input())
str_list = []
list_sort = []

for i in range(N):
    str_list.append(input())

list_set = list(set(str_list))

for j in list_set:
    list_sort.append((len(j), j))

result = sorted(list_sort)

for length, word in result:
    print(word)