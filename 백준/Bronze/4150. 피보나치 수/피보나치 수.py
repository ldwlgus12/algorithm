import sys
input = sys.stdin.readline

n = int(input())
fibo = [0, 1, 1]

for i in range(3, n+1):
    nums = fibo[i-1] + fibo[i-2]
    fibo.append(nums)
    
print(fibo[n])
