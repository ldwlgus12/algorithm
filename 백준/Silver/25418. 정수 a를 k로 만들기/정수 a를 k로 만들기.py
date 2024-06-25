a, k = map(int, input().split())
result = 0

while True:
    if a == k:
        print(result)
        break
    if k % 2 == 0 and k >= a*2:
        k = int(k/2)
    else:
        k -= 1
        
    result += 1
    