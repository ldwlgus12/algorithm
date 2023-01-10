T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    a = round(sum(num)/len(num))
    print(f"#{t} {a}")