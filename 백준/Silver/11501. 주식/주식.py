t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    max_data = data[-1]
    result = 0 
    
    for j in range(n-2, -1, -1):
        if data[j] > max_data:
            max_data = data[j]
        else:
            result += max_data - data[j]
            
    print(result)