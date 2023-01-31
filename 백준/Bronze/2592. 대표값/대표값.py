from collections import Counter
ave = 0
N_list = []

for i in range(10):
    N = int(input())
    N_list.append(N)
    ave += N

cnt = Counter(N_list)
result = cnt.most_common(1)

print(ave//10)
print(result[0][0])