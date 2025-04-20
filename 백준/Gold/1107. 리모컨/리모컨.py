import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))
result = abs(100-n)

for i in range(1000001):
    i = str(i)
    
    for j in range(len(i)):
        if int(i[j]) in broken:
            break            
        elif j == len(i)-1:
            result = min(result, abs(int(i)-n) + len(i))

print(result)
