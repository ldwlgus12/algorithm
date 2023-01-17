x, y = map(int, input().split())
x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())

x_list = (x, x_1, x_2)
y_list = (y, y_1, y_2)

if x_list[0] == x_list[1]:
    print(x_list[2], end=' ')
elif x_list[0] == x_list[2]:
    print(x_list[1], end=' ')
elif x_list[1] == x_list[2]:
    print(x_list[0], end=' ')

if y_list[0] == y_list[1]:
    print(y_list[2], end=' ')
elif y_list[0] == y_list[2]:
    print(y_list[1], end=' ')
elif y_list[1] == y_list[2]:
    print(y_list[0], end=' ')