import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())
sushi = [int(input()) for _ in range(n)]
result = 0

for i in range(n):
    if i+k > n:
        num_type = len(set(sushi[i:n] + sushi[:(i+k)%n] + [c]))
    else:
        num_type = len(set(sushi[i:i+k] + [c]))

    if result < num_type:
        result = num_type

print(result)
