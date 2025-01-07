for i in range(int(input())):
    n1, n2 = input().split()
    print(bin(int(n1, 2) + int(n2, 2))[2:])
    