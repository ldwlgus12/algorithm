import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
s_lst = sorted(set(lst))

dict = {s_lst[i]:i for i in range(len(s_lst))}

for j in lst:
    print(dict[j], end = ' ')
    