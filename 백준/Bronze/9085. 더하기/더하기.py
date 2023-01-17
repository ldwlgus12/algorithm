T = int(input())

for i in range(1, T+1): 
    N = int(input())
    X = list(map(int, input().split()))
    print(sum(X))