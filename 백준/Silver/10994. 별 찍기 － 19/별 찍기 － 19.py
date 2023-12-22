n = int(input())

for i in range(n - 1):
    print("* " * i + "*" * (1+4*(n-i-1)) + " *" * i)
    print("* " * (i+1) + " " * (1+4*(n-i-2)) + " *" * (i+1))
print("* " * (2*n-1))

for j in range(n - 1):
    print("* " * (n-j-1) + " " * (1+4*j) + " *" * (n-j-1))
    print("* " * (n-j-2) + "*" * (1+4*(j+1)) + " *" * (n-j-2))
