t = int(input())

for i in range(t):
    n = input().split()
    print(f"Case #{i+1}: {' '.join(n[::-1])}")