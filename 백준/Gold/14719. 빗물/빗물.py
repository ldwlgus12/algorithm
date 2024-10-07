h, w = map(int, input().split())
height = list(map(int, input().split()))
result = 0

for i in range(1, w-1):
    l_max = max(height[:i])
    r_max = max(height[i+1:])

    m = min(l_max, r_max)

    if height[i] < m:
        result += m - height[i]

print(result)
