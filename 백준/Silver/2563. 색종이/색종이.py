n = int(input())
ary = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            ary[i][j] = 1

for i in ary:
    result += i.count(1)
    
print(result)