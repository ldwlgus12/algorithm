dic = {'.': 46, 'O': 79, 
       '-': 124, '|': 45, 
       '/': 92, '\\': 47, 
       '^': 60, '<': 118, 
       'v': 62, '>': 94}

n, m = map(int, input().split())
box = [input() for _ in range(n)]
rotate = []

for i in range(m-1, -1, -1):
    row = []
    for j in range(n):
        row.append('%c' % dic[box[j][i]])
    rotate.append(row)
    
for i in rotate:
    print(''.join(i))
    