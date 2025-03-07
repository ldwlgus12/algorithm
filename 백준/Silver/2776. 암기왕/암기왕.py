import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    n_nums = set(map(int, input().split()))
    m = int(input())
    m_nums = list(map(int, input().split()))
    for i in m_nums:
        if i in n_nums:
            print(1)
        else:
            print(0)
            