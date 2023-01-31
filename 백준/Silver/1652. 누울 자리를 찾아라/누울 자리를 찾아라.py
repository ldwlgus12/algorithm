N = int(input())
bed = []
last = 0
last2 = 0

for _ in range(N):
    string = input()
    bed.append(string)

for i in range(N):
    result = 0

    for j in range(N):
        if bed[i][j] == '.':
            result += 1
        else:
            if result >= 2:
                last += 1
            result = 0

    if result >= 2:
        last += 1    


for i in range(N):
    result2 = 0

    for j in range(N):
        if bed[j][i] == '.':
            result2 += 1
        else:
            if result2 >= 2:
                last2 += 1
            result2 = 0
            
    if result2 >= 2:
        last2 += 1

print(last, last2)