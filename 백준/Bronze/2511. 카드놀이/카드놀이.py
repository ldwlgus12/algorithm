a_num = list(map(int, input('').split()))
b_num = list(map(int, input('').split()))

a, b = 0, 0
a_cnt, b_cnt = 0, 0

for i in range(10):
    if a_num[i] > b_num[i]:
        a = a + 3
        a_cnt = a_cnt + 1
        check = 'A'
    elif b_num[i] > a_num[i]:
        b = b + 3
        b_cnt = b_cnt + 1
        check = 'B'
    else:
        a = a + 1
        b = b + 1

if a_cnt > b_cnt:
    print(a, b)
    print('A')
elif b_cnt > a_cnt:
    print(a, b)
    print('B')
elif a_num == b_num:
    print(10, 10)
    print('D')
else:
    print(a, b)
    print(check)
    