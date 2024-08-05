import sys
input = sys.stdin.readline

n = int(input())
card_nums = list(map(int, input().split()))

m = int(input())
card_cnt = list(map(int, input().split()))

result = {}

for i in card_nums:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for i in card_cnt:
    if i in result:
        print(result[i], end=' ')
    else:
        print(0, end=' ')
