n = int(input())
rnd1 = list(map(int, input().split()))
rnd2 = list(map(int, input().split()))
Sum = 0

for i in rnd1:
    Sum += abs(i)
    
for i in rnd2:
    Sum += abs(i)
    
print(Sum)
