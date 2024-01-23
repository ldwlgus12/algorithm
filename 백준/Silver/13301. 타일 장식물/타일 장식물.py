n = int(input())

tile = [0] * 81
tile[0] = 4
tile[1] = 6

for i in range(2, n+1):
    tile[i] = tile[i-1] + tile[i-2]

print(tile[n-1])