n = int(input())
cookie = [input() for _ in range(n)]
heart = []
l_arm, r_arm, waist, l_leg, r_leg = 0, 0, 0, 0, 0
length = 0

for i in range(n):
    for j in range(n):
        if cookie[i][j] == "*":
            heart = [i+2, j+1]
            break
    if len(heart) > 0:
        break
        
for i in range(heart[1]-1):
    if cookie[heart[0]-1][i] == '*':
        l_arm += 1

for i in range(heart[1], n):
    if cookie[heart[0]-1][i] == '*':
        r_arm += 1

for i in range(heart[0], n):
    if cookie[i][heart[1]-1] == '*':
        waist += 1
        length = i

for i in range(n-1, length, -1):
    if cookie[i][heart[1]-2] == "*":
        l_leg += 1

for i in range(n-1, length, -1):
    if cookie[i][heart[1]] == "*":
        r_leg += 1
        
print(*heart)
print(l_arm, r_arm, waist, l_leg, r_leg)
