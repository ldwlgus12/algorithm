T = int(input())

for i in range(1, T+1):
    string = input()
    string_list = list(string)

    for j in range(len(string_list)):
        if 'b' in string_list[j]:
            string_list[j] = 'd'
        elif 'd' in string_list[j]:
            string_list[j] = 'b'
        elif 'p' in string_list[j]:
            string_list[j] = 'q'
        elif 'q' in string_list[j]:
            string_list[j] = 'p'

    print(f"#{i} {''.join(string_list[::-1])}")

