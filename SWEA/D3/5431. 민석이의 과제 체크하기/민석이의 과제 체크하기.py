T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    num_list = [a for a in range(1, N+1)]

    for b in range(len(num)):
        num_list.remove(num[b])

    print(f'#{i}',*num_list)