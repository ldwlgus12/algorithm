import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ice = [0] * 1000001
end = 0

for i in range(n):
    g, x = map(int, input().split())
    ice[x] = g
    end = max(end, x)

step = 2 * k + 1
w = sum(ice[:step])
result = w

for i in range(step, end+1):
    w += ice[i] - ice[i-step]
    result = max(result, w)
    
print(result)
