n = int(input())
size = list(map(int, input().split()))
score = 0

for i in range(len(size)-1):
    score += (size[i] * size[i+1])
    size[i+1] = size[i] + size[i+1]
    
print(score)
