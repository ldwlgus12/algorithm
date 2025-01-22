n, r, c = map(int, input().split())

if (r+c) % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            print("v." * (n//2) + 'v' * (n%2))
        else:
            print(".v" * (n//2) + '.' * (n%2))            
else:
    for i in range(n):
        if i % 2 == 1:
            print("v." * (n//2) + 'v' * (n%2))
        else:
            print(".v" * (n//2) + '.' * (n%2))
            