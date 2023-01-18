T = int(input())

for i in range(1, T+1):
    A, B = input().split()
    B_list = list(B)

    for j in range(len(B)):
        print(B[j] * int(A), end='')
    print('')