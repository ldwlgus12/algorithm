m, n = map(int, input().split())
size = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for i in range(m):
    for j in range(m):
        size_sort = sorted(size[j])
        idx = []
        
        for k in size[j]:
            idx.append(size_sort.index(k)+1)
        size[j] = idx

for i in range(m-1):
    for j in range(i+1, m):
        if size[i] == size[j]:
            cnt += 1

print(cnt)
