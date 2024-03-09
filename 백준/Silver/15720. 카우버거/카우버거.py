import sys
b, c, d = map(int, sys.stdin.readline().rstrip().split())

bp = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
cp = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
dp = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

beforePrice = sum(bp) + sum(cp) + sum(dp)
minCnt = min(len(bp), len(cp), len(dp))
afterPrice = beforePrice - (sum(bp[:minCnt]) + sum(cp[:minCnt]) + sum(dp[:minCnt])) // 10

print(beforePrice)
print(afterPrice)
