a, b = input().split()

ar = a[::-1]
br = b[::-1]
num = str(int(ar) + int(br))

print(int(num[::-1]))