import sys
n = int(sys.stdin.readline())
result = [0] * n

array = list(map(int, sys.stdin.readline().split()))
s_array = sorted(array)

for i in range(n):
  s_index = s_array.index(array[i])
  result[i] = s_index
  s_array[s_index] = -1

print(*result)