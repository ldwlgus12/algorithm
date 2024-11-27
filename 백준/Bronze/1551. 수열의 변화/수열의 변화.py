n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

for i in range(k):
    lst = []
    
    for j in range(1, len(arr)):
        lst.append(arr[j] - arr[j-1])
    arr = lst
    
print(*arr, sep=',')
