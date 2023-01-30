import sys
result = []

for i in range(1, 6):
    
    score = list(map(int, sys.stdin.readline().split()))
    result.append((sum(score), i))

result = sorted(result)

print(*result[4][::-1])