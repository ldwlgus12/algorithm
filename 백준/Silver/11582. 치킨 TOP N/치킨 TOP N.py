import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
k = int(input())
 
idx = n // k
lst = []
 
for i in range(0, n, idx):
    lst = c[i:i+idx]
    lst.sort()
    
    for j in lst:
        print(j, end=' ')
        