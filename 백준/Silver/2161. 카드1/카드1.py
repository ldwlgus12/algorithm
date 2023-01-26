N = int(input())

N_list = list(range(1, N+1))
dis = []

while len(N_list) > 1:
    dis.append(N_list.pop(0))
    N_list.append(N_list.pop(0))

print(*dis, N_list[0])