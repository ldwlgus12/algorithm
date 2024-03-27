n1, n2 = map(int, input().split())
g1 = list(input())
g2 = list(input())
t = int(input())
path = g1[::-1] + g2

for i in range(t):
    for j in range(len(path)-1):
        if path[j] in g1 and path[j+1] in g2:
            path[j], path[j+1] = path[j+1], path[j]
            if path[j+1] == g1[0]:
                break
                
print(''.join(path))
