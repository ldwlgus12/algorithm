n = list(map(int, input().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]

if n == a:
    print('ascending')
elif n == a[::-1]:
    print('descending')
else:
    print('mixed')