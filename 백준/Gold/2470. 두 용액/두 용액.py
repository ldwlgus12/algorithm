n = int(input())
lst = list(map(int, input().split(' ')))
lst.sort()

left = 0
right = n-1

abs_result = abs(lst[left] + lst[right])
result = [lst[left], lst[right]]


while left < right:
    l = lst[left]
    r = lst[right]

    Sum = l + r
  
    if abs(Sum) < abs_result:
        abs_result = abs(Sum)
        result = [l, r]
        
        if abs_result == 0:
          break
        
    if Sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
