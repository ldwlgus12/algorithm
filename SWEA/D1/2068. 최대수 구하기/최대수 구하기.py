T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    max_num = max(num)
    print(f"#{t} {max_num}")