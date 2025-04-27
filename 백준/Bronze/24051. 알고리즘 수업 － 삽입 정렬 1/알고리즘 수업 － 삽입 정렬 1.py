import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def insertion_sort(lst, k):
    cnt = 0

    for i in range(1, len(lst)):
        loc = i - 1
        newItem = lst[i]

        while loc >= 0 and newItem < lst[loc]:
            cnt += 1
            lst[loc+1] = lst[loc]
            loc -= 1

            if cnt == k:
                print(lst[loc+1])
                return

        if loc + 1 != i:
            cnt += 1
            lst[loc+1] = newItem

            if cnt == k:
                print(lst[loc+1])
                return
    print(-1)

insertion_sort(a, k)
