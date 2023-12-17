import sys
n, m = map(int, sys.stdin.readline().split(' '))
memo = {}
result = 0

for i in range(n):
    memo[sys.stdin.readline().rstrip()] = 1
    result += 1

for j in range(m):
    word = list(sys.stdin.readline().rstrip().split(','))
    for k in word:
        if k in memo.keys():
            if memo[k] == 1:
                memo[k] = 0
                result -= 1
    print(result)