import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

cnt_odd, cnt_even = 0, 0 
odd, even = 0, 0

for i in a:
  if i%2 == 1:
    cnt_odd += 1
    odd += cnt_even
  else:
    even += cnt_odd
    cnt_even += 1

print(min(even, odd))
