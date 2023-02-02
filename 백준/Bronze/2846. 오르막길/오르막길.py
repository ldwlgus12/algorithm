N = int(input())
high = []
a = 0
size = 0
size_list = []

num = list(map(int, input().split()))

for i in range(len(num)):
    if num[i] > a:
        a = num[i]
        high.append(a)
        high.sort(reverse=True)
        
    else:
        size = high[0] - high[-1]
        size_list.append(size)
        high = []
        a = num[i]
        high.append(a)

size_list.append(high[0] - high[-1])

print(max(size_list))