t = int(input())
test = [input() for _ in range(t)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in test:
    d = 0
    x, y = 0, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0

    for j in i:
        if j == "F":
            x += dx[d]
            y += dy[d]

        elif j == "B":
            x -= dx[d]
            y -= dy[d]
        
        elif j == "L":
            if d == 3:
                d = 0
            else:
                d += 1

        elif j == "R":
            if d == 0:
                d = 3
            else:
                d -= 1

        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

    print(abs(max_x-min_x) * abs(max_y-min_y))
    