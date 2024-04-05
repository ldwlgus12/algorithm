def light(lst, mid):
    if lst[1] - lst[0] > mid:
        return 0
    if lst[-1] - lst[-2] > mid:
        return 0
    
    for i in range(1, len(lst)-2):
        if (lst[i+1]-lst[i]) / 2 > mid:
            return 0
    return 1

n, m = int(input()), int(input())
lst = [0] + list(map(int, input().split())) + [n]

start, end = 0, n
result = 0

while start <= end:
    mid = (start+end) // 2
    if light(lst, mid):
        end = mid - 1
        result = mid
    else:
        start = mid + 1
        
print(result)
