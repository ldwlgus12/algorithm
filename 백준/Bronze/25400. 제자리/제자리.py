from collections import deque
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = deque(list(map(int, input().split())))
num = 1
cnt = 0

while q:
    a = q.popleft()
    if a == num:
        num += 1
    else:
        cnt += 1

print(cnt)
