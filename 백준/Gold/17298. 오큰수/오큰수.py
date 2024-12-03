import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

nge = [-1] * n
stack = []
stack.append(0)

for i in range(1, n):
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i]
    stack.append(i)

print(*nge)
