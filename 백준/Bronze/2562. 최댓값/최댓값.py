num = []

for i in range(9):
    N = int(input())
    num.append(N)

for j in range(9):
    if num[j] == max(num):
        print(num[j])
        print(j+1)