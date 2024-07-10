n = int(input())
stair = [[0] * 10 for _ in range(n)]
stair[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    stair[i][0] = stair[i-1][1]
    stair[i][9] = stair[i-1][8]    
    
    for j in range(1, 9):
        stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]
        
print(sum(stair[n-1]) % 1000000000)
