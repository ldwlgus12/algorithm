N_list = []

for i in range(10):
    N = int(input())
    N_list.append(N%42)

N_set = set(N_list)
print(len(N_set))