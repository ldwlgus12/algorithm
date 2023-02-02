w = []
k = []

for i in range(20):
    n = int(input())
    if i >= 10:
        k.append(n)
    else:
        w.append(n)

w_sort = sorted(w)
k_sort = sorted(k)

w_sum = w_sort[-3:]
k_sum = k_sort[-3:]

print(sum(w_sum), sum(k_sum))