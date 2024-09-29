t = int(input())

for i in range(t):
    n = int(input())
    loc = sorted(map(int, input().split()))
    
    print((loc[-1]-loc[0]) * 2)
    