r, c, zr, zc = map(int, input().split())
paper = [input() for _ in range(r)]
scan = []

for i in range(r):
    lst = []
    for j in range(c):
        lst.append(paper[i][j] * zc)
    for k in range(zr):
        scan.append(lst)

for i in scan:
    print("".join(i))
    