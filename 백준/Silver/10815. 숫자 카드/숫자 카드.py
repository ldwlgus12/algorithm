import sys
n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic = {} 

for i in range(len(card)):
    dic[card[i]] = 0  

for j in range(m):
    if check[j] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')