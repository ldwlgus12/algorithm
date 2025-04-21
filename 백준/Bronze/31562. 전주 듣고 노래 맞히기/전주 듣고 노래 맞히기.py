n, m = map(int, input().split())
song = {}

for _ in range(n):
    t, s, a1, a2, a3, a4, a5, a6, a7 = input().split()
    first = [a1, a2, a3]
    song[s] = first

for _ in range(m):
    b = input().split()
    same_cnt = 0
    title = ""

    for i in song:
        if b == song[i]:
            same_cnt += 1
            title = i

    if same_cnt >= 2:
        print("?")
    elif same_cnt == 1:
        print(title)
    else:
        print("!")
        