T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    A = a//b
    B = a%b
    print(f"#{t} {A} {B}")