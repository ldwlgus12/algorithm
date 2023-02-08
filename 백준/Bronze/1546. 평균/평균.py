x = int(input())
y = list(map(int, input().split()))
m = max(y)
hap = 0

for i in range(len(y)):
    score = ((y[i]/m) * 100)
    hap += score
print(hap/x)