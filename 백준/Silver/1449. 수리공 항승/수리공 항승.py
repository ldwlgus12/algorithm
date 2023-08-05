import sys
n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split(' ')))
arr.sort()

s = arr[0] - 0.5
e = s + l
cnt = 1

for i in range(0, len(arr)): 
  if s < arr[i] < e:
    continue
  else:
    cnt += 1
    s = arr[i] - 0.5
    e = s + l

print(cnt)