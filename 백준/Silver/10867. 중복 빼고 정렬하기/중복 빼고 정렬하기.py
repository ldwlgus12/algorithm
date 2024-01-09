n = int(input())
lst = list(map(int, input().split()))
s_lst = sorted(set(lst))

for i in s_lst:
    print(i, end = ' ')
