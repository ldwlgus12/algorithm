import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

lst = []

for i in range(0, n-1):
    lst.append(sensor[i+1] - sensor[i])

lst.sort()

print(sum(lst[:n-k]))
